import sys
import pandas as pd
import os  

file_path = sys.argv[1]

df = pd.read_csv(file_path)

output_path = "data_raw.csv"
df.to_csv(output_path, index=False)

print("Data saved as data_raw.csv")

os.system(f"py preprocess.py {output_path}")
