import pandas as pd

def shuffle_csv(csv_path, shuffled_csv_path):
    try:
        print(f"Reading CSV file from: {csv_path}")
        df = pd.read_csv(csv_path)
        if df.empty:
            print("The CSV file is empty.")
            return
        print("CSV file read successfully.")
        print(f"Data in CSV file: \n{df.head()}") 
        
        print("Shuffling data...")
        shuffled_df = df.sample(frac=1).reset_index(drop=True)
        print("Data shuffled successfully.")
        
        print(f"Writing shuffled data to: {shuffled_csv_path}")
        shuffled_df.to_csv(shuffled_csv_path, index=False)
        print("Shuffled data has been written to the new CSV file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_path = r'D:\Licenta\Licenta\Cloud\generate_dataset\start10.csv'
shuffled_csv_path = r'D:\Licenta\Licenta\Cloud\generate_dataset\shuffle.csv'
shuffle_csv(csv_path, shuffled_csv_path)
