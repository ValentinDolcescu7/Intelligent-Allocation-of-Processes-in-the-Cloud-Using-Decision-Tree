import pandas as pd

def remove_duplicate_rows(csv_file, columns_to_check):
    df = pd.read_csv(csv_file)

    df_unique = df.drop_duplicates(subset=columns_to_check, keep='first')
    
    return df_unique

csv_file = r'D:\Licenta\Licenta\Cloud\generate_dataset\shuffle.csv'
columns_to_check = ["Instructions", "Size", "Priority", "Bandwidth", "Delay", "Score"]
df_unique = remove_duplicate_rows(csv_file, columns_to_check)

df_unique.to_csv(r'D:\Licenta\Licenta\Cloud\dataset_final.csv', index=False)

print("The script was saved!")
