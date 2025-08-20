import pandas as pd

def format_csv(input_path, output_path):
    df = pd.read_csv(input_path)
    df.dropna(inplace=True)
    df.columns = [col.strip().title() for col in df.columns]
    df.to_csv(output_path, index=False)