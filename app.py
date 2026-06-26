import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Railway Data Engineering Dashboard")

# Load dataset
df = pd.read_csv("Railway_info.csv")


option = st.sidebar.selectbox(
    "Select Task",
    (
        "Dataset Preview",
        "Basic Statistics",
        "Data Cleaning",
        "Visualization"
    )
)


if option == "Dataset Preview":
    st.header("First 10 Rows")
    st.dataframe(df.head(10))

    st.header("Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.header("Missing Values")
    st.write(df.isnull().sum())


elif option == "Basic Statistics":
    st.header("Statistics")

    st.write("Total Trains:", df["Train_No"].nunique())
    st.write("Unique Source Stations:",
             df["Source_Station_Name"].nunique())
    st.write("Unique Destination Stations:",
             df["Destination_Station_Name"].nunique())

    st.subheader("Most Common Source Stations")
    st.write(df["Source_Station_Name"].value_counts().head())

    st.subheader("Most Common Destination Stations")
    st.write(df["Destination_Station_Name"].value_counts().head())


elif option == "Data Cleaning":
    cleaned_df = df.copy()

    cleaned_df["Source_Station_Name"] = (
        cleaned_df["Source_Station_Name"].str.upper()
    )

    cleaned_df["Destination_Station_Name"] = (
        cleaned_df["Destination_Station_Name"].str.upper()
    )

    cleaned_df.dropna(inplace=True)

    st.success("Data cleaned successfully!")
    st.dataframe(cleaned_df.head())


elif option == "Visualization":
    st.header("Train Distribution by Source Station")

    counts = (
        df["Source_Station_Name"]
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)

    plt.xticks(rotation=90)
    st.pyplot(fig)