import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

print("===== TASK 2: TRANSFORMATION =====")

# 🔹 2.1 Filter trains running on Saturday
saturday_trains = df[df['days'] == "Saturday"]
print("\nSaturday trains:")
print(saturday_trains.head())

# 🔹 Filter trains from a specific station
station_name = "MADGOAN JN."   # you can change this
from_station = df[df['Source_Station_Name'] == station_name]
print(f"\nTrains from {station_name}:")
print(from_station.head())

# 🔹 2.2 Grouping: count trains per source station
grouped = df.groupby('Source_Station_Name').size()
print("\nTrain count per source station:")
print(grouped.head())

# 🔹 Average trains per day (based on 'days' column)
avg_trains = df.groupby('Source_Station_Name')['days'].count()
print("\nAverage trains per station (based on frequency):")
print(avg_trains.head())

# 🔹 2.3 Data Enrichment (Weekday / Weekend)

def categorize(day):
    if day in ["Saturday", "Sunday"]:
        return "Weekend"
    else:
        return "Weekday"

df['Train_Category'] = df['days'].apply(categorize)

print("\nAdded Category Column:")
print(df[['Source_Station_Name', 'days', 'Train_Category']].head())

# Save transformed data
df.to_csv("transformed_data.csv", index=False)

print("\n✅ Task 2 Completed. File saved as transformed_data.csv")