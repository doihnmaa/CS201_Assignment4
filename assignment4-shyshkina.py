import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("random_walk.csv")
print(df.head()) #хед це перші 5 рядків таблиці. від 0 починається

df["distance"] = np.sqrt(df["x"]**2 + df["y"]**2) #відстань векторно
print(df.head())

max_distance = df["distance"].max() #максимальна відстань
avg_distance = df["distance"].mean() #середня відстань
print(f"\nмаксимальна відстань: {max_distance:.2f}")
print(f"середня відстань: {avg_distance:.2f}")

filtered = df[df["distance"] > avg_distance] #відстань до центру є більшою, ніж середнє значення
print(filtered)

# filtered.to_json("filtered_walk.json", orient="records", indent=4) #береження джсон

plt.figure(figsize=(8, 4))
plt.plot(df["x"], df["y"], color="purple")
plt.show()