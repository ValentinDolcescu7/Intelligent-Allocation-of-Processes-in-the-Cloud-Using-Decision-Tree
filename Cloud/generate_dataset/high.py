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
    bandwidth_high = np.random.randint(51, 101)  
    return [bandwidth_high]

def generate_delay():
    delay_high = np.random.randint(1, 31)
    return [delay_high]

def generate_dataset(num_samples=30000, csv_path=r'D:\Licenta\Licenta\Cloud\generate_dataset\start10.csv', batch_size=1000):
    buffer = []  
    
    for _ in range(num_samples):
        instructions = np.random.randint(1, 101)
        size = np.random.randint(1, 11)
        bandwidths = generate_bandwidths()
        delays = generate_delay()
        
        score_high = find_score_in_csv(bandwidths[0], delays[0], r'D:\Licenta\Licenta\Cloud\generate_dataset\high_score.csv')
    
        
        row = {
            'Area': np.random.choice([1, 2, 3]),
            'Instructions': instructions,
            'Size': size,
            'Priority': 1.0,
            'Bandwidth': bandwidths[0],
            'Delay': delays[0],
            'Score': score_high,
            'Allocated_Worker': 1
        }
        buffer.append(row)
        
        if len(buffer) == batch_size or _ == num_samples - 1:
            df_buffer = pd.DataFrame(buffer)
            df_buffer.to_csv(csv_path, mode='a', index=False, header=not _, encoding='utf-8-sig')
            buffer = []  
            print(f"Am generat și scris {len(df_buffer)} de date în fisier.")

    print("Generarea datelor pentru high priority tasks a fost finalizata.")

generate_dataset()