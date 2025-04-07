import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Web App
st.title("📊 Smart Data Processing & Reporting Tool")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Function to Clean Data
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df

# Function to Generate Summary Report
def generate_report(df):
    report = df.describe(include='all')
    missing_values = df.isnull().sum()
    unique_counts = df.nunique()
    
    st.subheader("📋 Summary Report")
    st.write(report)

    st.subheader("🔍 Missing Values")
    st.write(missing_values)

    st.subheader("📌 Unique Value Counts")
    st.write(unique_counts)

# Function to Plot Charts
def plot_charts(df):
    st.subheader("📈 Data Visualizations")
    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df[col], kde=True, color='skyblue', ax=ax)
        plt.title(f'Distribution of {col}')
        st.pyplot(fig)

# Processing Uploaded File
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Cleaning Data
    df_clean = clean_data(df)

    # Show Summary Report
    generate_report(df_clean)

    # Show Visualizations
    plot_charts(df_clean)

    # Save Processed File for Download
    csv = df_clean.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Cleaned Data",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
