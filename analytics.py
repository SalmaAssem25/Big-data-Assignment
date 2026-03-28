import sys
import pandas as pd
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)


with open("insight1.txt", "w") as f:
    f.write(f"Dataset shape: {df.shape}")


with open("insight2.txt", "w") as f:
    f.write(f"Column names: {list(df.columns)}")


with open("insight3.txt", "w") as f:
    f.write(f"Summary statistics:\n{df.describe()}")

print("Insights generated successfully")


os.system(f"py visualize.py {file_path}")