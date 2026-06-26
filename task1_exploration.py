import pandas as pd

# Load dataset
df = pd.read_csv("Railway_info.csv")

# Show first 10 rows
print("===== FIRST 10 ROWS =====")
print(df.head(10))

# Dataset info
print("\n===== DATASET INFO =====")
print(df.info())

# Print column names (for safety)
print("\nColumns in dataset:")
print(df.columns)

# Basic statistics
print("\n===== BASIC STATISTICS =====")
print("Total number of trains:", len(df))

print("Unique Source Stations:", df['Source_Station_Name'].nunique())
print("Unique Destination Stations:", df['Destination_Station_Name'].nunique())

print("\nMost Common Source Station:")
print(df['Source_Station_Name'].value_counts().head(1))

print("\nMost Common Destination Station:")
print(df['Destination_Station_Name'].value_counts().head(1))

# Cleaning
print("\n===== DATA CLEANING =====")

df.fillna("UNKNOWN", inplace=True)

df['Source_Station_Name'] = df['Source_Station_Name'].str.upper()
df['Destination_Station_Name'] = df['Destination_Station_Name'].str.upper()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("✅ Cleaned data saved as cleaned_data.csv")