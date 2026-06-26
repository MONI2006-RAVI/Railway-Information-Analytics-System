import pandas as pd
import matplotlib.pyplot as plt

# Load transformed data
df = pd.read_csv("transformed_data.csv")

print("===== TASK 3: ANALYSIS =====")

# 🔹 3.1 Distribution of trains across days
day_counts = df['days'].value_counts()

print("\nTrain distribution across days:")
print(day_counts)

# Bar chart
plt.figure()
day_counts.plot(kind='bar')
plt.title("Train Distribution Across Days")
plt.xlabel("Days")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)
plt.show()

# 🔹 Pattern analysis (Top source stations)
top_sources = df['Source_Station_Name'].value_counts().head(10)

print("\nTop 10 busiest source stations:")
print(top_sources)

# 🔹 3.2 Correlation-style insight (manual since no numeric day columns)

print("\n===== INSIGHTS =====")

busiest_day = day_counts.idxmax()
least_day = day_counts.idxmin()

print(f"Busiest day: {busiest_day}")
print(f"Least busy day: {least_day}")

# Weekend vs Weekday comparison
weekend = df[df['Train_Category'] == "Weekend"].shape[0]
weekday = df[df['Train_Category'] == "Weekday"].shape[0]

print(f"\nWeekend trains: {weekend}")
print(f"Weekday trains: {weekday}")