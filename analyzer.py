import pandas as pd
import numpy as np

def load_data():
    return pd.read_csv('data/patient_records.csv')

def analyze_data(df):
    df['HR_Status'] = np.where((df['HeartRate'] < 60) | (df['HeartRate'] > 100), 'Abnormal', 'Normal')
    df['BP_Status'] = np.where((df['SystolicBP'] > 140) | (df['DiastolicBP'] > 90), 'High', 'Normal')
    df['Glucose_Status'] = np.where(df['Glucose'] > 140, 'High', 'Normal')
    df['Critical'] = np.where(
        (df['HR_Status'] == 'Abnormal') |
        (df['BP_Status'] == 'High') |
        (df['Glucose_Status'] == 'High'),
        'YES', 'NO'
    )
    return df

def save_results(df):
    df.to_csv('processed_results.csv', index=False)
    print("✔ Results saved to 'processed_results.csv'")

def filter_critical(df):
    return df[df['Critical'] == 'YES']

def filter_by_age(df, min_age):
    return df[df['Age'] >= min_age]

def cli_menu():
    print("\n🩺 Healthcare Patient Data Analyzer")
    print("1. View all analyzed results")
    print("2. View only critical patients")
    print("3. Filter patients by age")
    print("4. Save results to CSV")
    print("5. Exit")

def main():
    df = load_data()
    df = analyze_data(df)

    while True:
        cli_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print(df)
        elif choice == '2':
            print("\n🔴 Critical
