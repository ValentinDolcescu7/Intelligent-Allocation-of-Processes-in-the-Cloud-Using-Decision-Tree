import numpy as np
import pandas as pd

def calculate_score(bandwidth, delay):
    return (1 / bandwidth) + delay

def find_valid_combinations():
    valid_combinations = []
    for bandwidth in range(25, 51):
        for delay in range(31, 71):
            score = calculate_score(bandwidth, delay)
            valid_combinations.append((bandwidth, delay, score))
    return valid_combinations

def add_additional_column(combinations):
    additional_value = 70
    for index in range(len(combinations)):
        if index % 4 == 0 and index != 0:
            additional_value -= 0.153
        combinations[index] = combinations[index] + (additional_value,)
    return combinations

def round_to_decimal(combinations):
    rounded_combinations = []
    for combo in combinations:
        rounded_combo = tuple(round(value, 2) for value in combo)
        rounded_combinations.append(rounded_combo)
    return rounded_combinations

def save_to_csv(combinations, file_path):
    df = pd.DataFrame(combinations, columns=['Bandwidth', 'Delay', 'Score', 'Additional Value'])
    df.to_csv(file_path, index=False)
    print(f"Data has been saved to {file_path}")

valid_combinations = find_valid_combinations()
valid_combinations_sorted = sorted(valid_combinations, key=lambda x: x[2])
valid_combinations_sorted = add_additional_column(valid_combinations_sorted)
valid_combinations_sorted = round_to_decimal(valid_combinations_sorted)
save_to_csv(valid_combinations_sorted, r'D:\Licenta\Licenta\Cloud\generate_dataset\medium_score.csv')
