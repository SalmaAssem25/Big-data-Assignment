import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)


plt.figure()
df.hist()
plt.suptitle("Histogram of Features")
plt.savefig("histogram.png")


plt.figure()
plt.scatter(df["PC1"], df["PC2"])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Scatter Plot")
plt.savefig("scatter.png")


plt.figure()
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")



plt.figure(figsize=(15,10))

# 1. Histogram (ONLY PC1)
plt.subplot(2,2,1)
plt.hist(df["PC1"])
plt.title("Histogram of PC1")

# 2. Scatter
plt.subplot(2,2,2)
plt.scatter(df["PC1"], df["PC2"])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Scatter Plot")

# 3. Heatmap
plt.subplot(2,2,3)
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png")

print("Visualizations saved")


os.system(f"py cluster.py {file_path}")