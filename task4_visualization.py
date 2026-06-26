import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("transformed_data.csv")

print("===== TASK 4: VISUALIZATION =====")

# 🔹 1. Top 10 Source Stations
top_sources = df['Source_Station_Name'].value_counts().head(10)

plt.figure()
top_sources.plot(kind='bar')
plt.title("Top 10 Source Stations")
plt.xlabel("Station")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)
plt.show()


# 🔹 2. Train Distribution by Days
day_counts = df['days'].value_counts()

plt.figure()
day_counts.plot(kind='bar')
plt.title("Train Distribution by Days")
plt.xlabel("Days")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)
plt.show()


# 🔹 3. Weekday vs Weekend
category_counts = df['Train_Category'].value_counts()

plt.figure()
category_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Weekday vs Weekend Trains")
plt.ylabel("")   # removes extra label
plt.show()


print("\n✅ Task 4 Completed (All graphs displayed)")