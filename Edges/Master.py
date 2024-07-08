import os
import threading
from joblib import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Cloudlet import Cloudlet
import shutil  

class Master:
    def __init__(self):
        self.model = load(r'D:\Licenta\Licenta\allocated_worker_model.joblib')
        self.combinations = pd.read_csv(r'D:\Licenta\Licenta\Edges\workers\file.csv')

    def get_input(self):
        self.area = int(input("Introduceti zona: "))
        self.instructions = int(input("Introduceți numărul de instrucțiuni: "))
        self.size = int(input("Introduceți dimensiunea: "))
        self.priority = float(input("Introduceti prioritatea: "))
        self.bandwidth = int(input("Introduceți debitul: "))
        self.delay = int(input("Introduceți întârzierea: "))
        self.score = 1 / self.bandwidth + self.delay
        self.assign_score()

    def assign_score(self):
        for _, row in self.combinations.iterrows():
            if row['Bandwidth'] == self.bandwidth and row['Delay'] == self.delay:
                self.score = row['Additional Value']
                break

    def simulate_allocation(self):
        self.cloudlet = Cloudlet(
            area=self.area,
            instructions=self.instructions,
            size=self.size,
            priority=self.priority,
            bandwidth=self.bandwidth,
            delay=self.delay,
            score=self.score
        )

        data = pd.DataFrame([self.cloudlet.getAsDict()])


        data.columns = ['Area', 'Instructions', 'Size', 'Priority', 'Bandwidth', 'Delay', 'Score']

        print(f"Generated DataFrame:\n{data}")

        prediction_input = data[['Area', 'Instructions', 'Size', 'Priority', 'Bandwidth', 'Delay', 'Score']]

        print(f"Input pentru model: {prediction_input.to_dict('records')[0]}") 

        prediction = self.model.predict(prediction_input)[0]
        print(f"Predicție pentru Worker alocat: {prediction}")
        return prediction

    def create_folders(self, prediction):
        if prediction == 1:
            base_path = r'D:\Licenta\Licenta\Edges\workers\Worker1'
            max_folders = 100
        elif prediction == 2:
            base_path = r'D:\Licenta\Licenta\Edges\workers\Worker2'
            max_folders = 200
        elif prediction == 3:
            base_path = r'D:\Licenta\Licenta\Edges\workers\Worker3'
            max_folders = 300
        else:
            print("Predicție invalidă.")
            return

        for i in range(1, max_folders + 1):
            folder_path = os.path.join(base_path, f'Folder_{i}')
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                #print(f"Sters folder: {folder_path}")

        for i in range(1, self.instructions + 1):
            folder_path = os.path.join(base_path, f'Folder_{i}')
            os.makedirs(folder_path, exist_ok=True)
            print(f"Creat folder: {folder_path}")

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

nodes = {
    'zona1': (1, 5), 'zona2': (1, 7), 'zona3': (1, 3), 
    'master': (5, 5), 
    'muncitor1': (9, 7), 'muncitor2': (9, 5), 'muncitor3': (9, 3)
}

for node, (x, y) in nodes.items():
    ax.plot(x, y, 'o', label=node)
    ax.text(x, y, ' ' + node, verticalalignment='bottom', horizontalalignment='right')

task, = ax.plot([], [], 'ro')

path_x, path_y = [], []
frames_per_segment = 28
total_frames = 1 
task_at_master = threading.Event()
task_completed = threading.Event()

def init():
    task.set_data([], [])
    return task,

def animate(i):
    if not path_x or not path_y:
        return task,

    segment = i // frames_per_segment
    if segment < len(path_x) - 1:
        start_x, start_y = path_x[segment], path_y[segment]
        end_x, end_y = path_x[segment + 1], path_y[segment + 1]
        progress = (i % frames_per_segment) / frames_per_segment
        x = start_x + (end_x - start_x) * progress
        y = start_y + (end_y - start_y) * progress
        task.set_data([x], [y])
    else:
        if len(path_x) == 2: 
            task_at_master.set()
        else:  
            task_completed.set()
            ani.event_source.stop() 
    return task,

def frame_generator():
    global total_frames
    while True:
        yield from range(total_frames)

ani = FuncAnimation(fig, animate, frames=frame_generator, init_func=init, blit=True, repeat=False, save_count=total_frames)

def update_path(zone, target_node):
    global path_x, path_y, total_frames
    if target_node is None: 
        new_path = [nodes[f'zona{zone}'], nodes['master']]
    else: 
        new_path = [nodes['master'], nodes[f'muncitor{target_node}']]
    path_x, path_y = zip(*new_path)
    total_frames = (len(path_x) - 1) * frames_per_segment
    ani.event_source.stop()
    ani.frame_seq = ani.new_frame_seq()
    ani.event_source.start()

def input_thread(master):
    while True:
        master.get_input()
        update_path(master.area, None) 
        task_at_master.wait(5) 
        task_at_master.clear() 
        prediction = master.simulate_allocation()
        update_path(master.area, prediction) 
        task_completed.wait(5)
        master.create_folders(prediction)
        task_completed.clear()  
        reset_task_position()

def reset_task_position():
    task.set_data([], []) 
    plt.draw()
    ani.event_source.stop()

master = Master()
thread = threading.Thread(target=input_thread, args=(master,))
thread.daemon = True
thread.start()

plt.show()
