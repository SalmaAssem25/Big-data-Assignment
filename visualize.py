import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)

plt.figure(figsize=(15,10))

# 1. Histogram PC1
plt.subplot(2,2,1)
plt.hist(df["PC1"])
plt.title("Histogram of PC1")

# 2. Histogram PC2
plt.subplot(2,2,2)
plt.hist(df["PC2"])
plt.title("Histogram of PC2")

# 3. Scatter
plt.subplot(2,2,3)
plt.scatter(df["PC1"], df["PC2"])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Scatter Plot")

# 4. Heatmap
plt.subplot(2,2,4)
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png")

print("Visualizations saved")

os.system("python cluster.py data_preprocessed.csv")