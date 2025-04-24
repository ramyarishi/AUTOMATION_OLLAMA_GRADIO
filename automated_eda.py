import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform EDA and generate visualizations
def eda_analysis(df):
    # Fill missing values
    for col in df.select_dtypes(include=['number']).columns:
        df[col].fillna(df[col].median(), inplace=True)
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Data Summary
    summary = df.describe(include='all')

    # Missing Values
    missing_values = df.isnull().sum()

    # Generate Basic Insights (Simple analysis)
    insights = generate_basic_insights(df)

    # Generate Data Visualizations
    plot_paths = generate_visualizations(df)

    return summary, missing_values, insights, plot_paths

# Function to generate basic insights (e.g., column data types, correlation)
def generate_basic_insights(df):
    insights = []

    # Column Data Types
    insights.append("Column Data Types:\n" + str(df.dtypes))

    # Correlation Matrix for Numeric Features
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        correlations = numeric_df.corr()
        insights.append("\nCorrelation Matrix:\n" + str(correlations))

    # Value Counts for Categorical Columns
    categorical_df = df.select_dtypes(include=['object'])
    if not categorical_df.empty:
        for col in categorical_df.columns:
            insights.append(f"\nValue Counts for {col}:\n" + str(df[col].value_counts()))

    return "\n".join(insights)

# Function to generate data visualizations
def generate_visualizations(df):
    plot_paths = []

    # Histograms for Numeric Columns
    for col in df.select_dtypes(include=['number']).columns:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df[col], bins=30, kde=True, color="blue", ax=ax)
        ax.set_title(f"Distribution of {col}")
        path = f"{col}_distribution.png"
        fig.savefig(path)
        plot_paths.append(path)
        plt.close(fig)

    # Correlation Heatmap (only numeric columns)
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        fig, ax = plt.subplots(figsize=(8,5))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
        ax.set_title("Correlation Heatmap")
        path = "correlation_heatmap.png"
        fig.savefig(path)
        plot_paths.append(path)
        plt.close(fig)

    return plot_paths

# Streamlit Web App
def main():
    st.title("📊 Automated Exploratory Data Analysis (EDA)")

    # File Upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Perform EDA
        summary, missing_values, insights, plot_paths = eda_analysis(df)

        # Display Summary
        st.subheader("Dataset Summary")
        st.write(summary)

        # Display Missing Values
        st.subheader("Missing Values")
        st.write(missing_values)

        # Display Insights
        st.subheader("Basic Insights")
        st.write(insights)

        # Display Visualizations
        st.subheader("Visualizations")
        for plot_path in plot_paths:
            st.image(plot_path, caption=plot_path)

# Run the Streamlit app
if __name__ == "__main__":
    main()
