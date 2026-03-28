import sys
import pandas as pd
import numpy as np
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)

#cleaning data
df = df.fillna(df.mean(numeric_only=True))
df = df.drop_duplicates()

#Feature Transformation
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = scaler.fit_transform(df[num_cols]) 

#Dimensionality Reduction
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
df_pca = pca.fit_transform(df)

df = pd.DataFrame(df_pca, columns=["PC1", "PC2"])


#Discretization
df["PC1_bin"] = pd.cut(df["PC1"], bins=3, labels=["Low", "Medium", "High"])

output_path = "data_preprocessed.csv"
df.to_csv(output_path, index=False)
os.system(f"py analytics.py {output_path}")