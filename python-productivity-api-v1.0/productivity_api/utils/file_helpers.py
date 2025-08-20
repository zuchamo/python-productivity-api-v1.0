import os

def list_csv_files(folder):
    return [f for f in os.listdir(folder) if f.endswith('.csv')]