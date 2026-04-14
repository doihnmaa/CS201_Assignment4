import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("random_walk.csv")
print(df.head())

df["distance"] = np.sqrt(df["x"]**2 + df["y"]**2) #відстань векторно
print(df.head())

max_distance = df["distance"].max() #максимальна відстань
avg_distance = df["distance"].mean() #середня відстань
print(f"\nмаксимальна відстань: {max_distance:.2f}")
print(f"середня відстань: {avg_distance:.2f}")
