import pandas as pd
import numpy as np

def find_score_in_csv(bandwidth, delay, csv_path):
    df = pd.read_csv(csv_path)
    match = df[(df['Bandwidth'] == bandwidth) & (df['Delay'] == delay)]
    if not match.empty:
        additional_value = match.iloc[0]['Additional Value']
        return additional_value
    return None 

def generate_bandwidths():
    bandwidth_medium = np.random.randint(25, 51)  
    return [bandwidth_medium]

def generate_delay():
    delay_medium = np.random.randint(31, 71)
    return [delay_medium]

def generate_dataset(num_samples=30000, csv_path=r'D:\Licenta\Licenta\Cloud\generate_dataset\start10.csv', batch_size=1000):
    buffer = []  
    
    for _ in range(num_samples):
        instructions = np.random.randint(101, 201)
        size = np.random.randint(11, 21)
        bandwidths = generate_bandwidths()
        delays = generate_delay()
        
        score_medium = find_score_in_csv(bandwidths[0], delays[0], r'D:\Licenta\Licenta\Cloud\generate_dataset\medium_score.csv')
    
        
        row = {
            'Area': np.random.choice([1, 2, 3]),
            'Instructions': instructions,
            'Size': size,
            'Priority': 0.5,
            'Bandwidth': bandwidths[0],
            'Delay': delays[0],
            'Score': score_medium,
            'Allocated_Worker': 2
        }
        buffer.append(row)
        
        if len(buffer) == batch_size or _ == num_samples - 1:
            df_buffer = pd.DataFrame(buffer)
            df_buffer.to_csv(csv_path, mode='a', index=False, header=not _, encoding='utf-8-sig')
            buffer = []  
            print(f"Am generat si scris {len(df_buffer)} de date în fisier.")

    print("Generarea datelor pentru medium priority tasks a fost finalizata.")

generate_dataset()