import sys
import pandas as pd
from sklearn.cluster import KMeans
import os


file_path = sys.argv[1]
df = pd.read_csv(file_path)


kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['PC1', 'PC2']])


df['cluster'].value_counts().to_csv("clusters.txt", header=False)