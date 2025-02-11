
import pandas as pd  # Importing pandas for data manipulation
import streamlit as st  # Importing Streamlit for building the web app
import plotly.express as px  # Importing Plotly for interactive visualizations
import matplotlib.pyplot as plt  # Importing Matplotlib for static plots
import seaborn as sns  # Importing Seaborn for statistical visualizations

# Set up the page configuration
st.set_page_config(
    layout="wide",  # Setting layout to wide for better visualization
    page_title="911 Calls Dashboard 🚨",  # Setting the page title
    page_icon="🚔"  # Setting the page icon
)

# Load dataset
df = pd.read_csv("cleaned_dataset_911.csv")  # Loading the cleaned dataset

# Convert timeStamp column to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])  # Converting timestamp to datetime format

# Extract additional time-based features
df["Year"] = df["timestamp"].dt.year  # Extracting year from timestamp
df["Month"] = df["timestamp"].dt.month  # Extracting month from timestamp
df["Hour"] = df["timestamp"].dt.hour  # Extracting hour from timestamp
df["Day"] = df["timestamp"].dt.dayofweek  # Extracting day of the week

# Extract emergency type from the title column
df["Reason"] = df["title"].apply(lambda x: x.split(":")[0])  # Extracting emergency type

# Title of the dashboard
st.title("📊 911 Calls Analysis Dashboard 🚨")  # Displaying the dashboard title
st.markdown("Interactive analysis of emergency calls in Montgomery County using open Kaggle data.")  # Dashboard description

# ---- KPIs ----
st.markdown("## 🔥 Key Metrics")  # Section for key metrics

# Creating columns for KPIs
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    total_calls = df.shape[0]  # Calculating total number of calls
    st.metric("Total Calls", f"{total_calls:,}")  # Displaying total calls metric

with kpi_col2:
    top_reason = df["Reason"].value_counts().idxmax()  # Finding the most common emergency type
    st.metric("Most Common Emergency", top_reason)  # Displaying the most common emergency

with kpi_col3:
    top_city = df["township"].value_counts().idxmax()  # Finding the city with the most calls
    st.metric("City with Most Calls", top_city)  # Displaying the city with the most calls

with kpi_col4:
    peak_hour = df["Hour"].value_counts().idxmax()  # Finding the peak hour for calls
    st.metric("Peak Call Hour", f"{peak_hour}:00")  # Displaying the peak call hour

# ---- SIDEBAR FILTERS ----
st.sidebar.header("🔍 Filters")  # Sidebar filters section

# Sidebar filters to select emergency type, city, and year
selected_reason = st.sidebar.multiselect("Select Emergency Type:", options=df["Reason"].unique(), default=df["Reason"].unique())
selected_city = st.sidebar.multiselect("Select City:", options=df["township"].unique(), default=df["township"].unique())
selected_year = st.sidebar.multiselect("Select Year:", options=df["Year"].unique(), default=df["Year"].unique())

# Apply the selected filters to the dataframe
filtered_df = df[
    (df["Reason"].isin(selected_reason)) &
    (df["township"].isin(selected_city)) &
    (df["Year"].isin(selected_year))
]

# ---- GRAPHS & VISUALIZATIONS ----
tab1, tab2, tab3 = st.tabs(["📈 Trends", "📍 Map View", "📊 Descriptive Stats"])

# *Tab 1: Trends & Analysis*
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        city_calls = filtered_df["township"].value_counts().nlargest(10)  # Top 10 cities with most calls
        fig2 = px.bar(city_calls, x=city_calls.index, y=city_calls.values, title="🏩 Top 10 Cities with Most Calls", labels={"x": "City", "y": "Number of Calls"})
        st.plotly_chart(fig2, use_container_width=True)

        fig3 = px.histogram(filtered_df, x="Year", title="📅 Call Distribution by Year")  # Calls by year
        st.plotly_chart(fig3, use_container_width=True)

        emergency_calls = filtered_df["Reason"].value_counts()  # Emergency type breakdown
        fig7 = px.bar(emergency_calls, x=emergency_calls.index, y=emergency_calls.values, title="🚨 Emergency Calls Breakdown", labels={"x": "Emergency Type", "y": "Number of Calls"})
        st.plotly_chart(fig7, use_container_width=True)

    with col2:
        fig5 = px.pie(filtered_df, names="Reason", title="🚨 Emergency Calls Breakdown")  # Pie chart for emergency types
        st.plotly_chart(fig5, use_container_width=True)

        fig6 = plt.figure(figsize=(8, 4))  # Boxplot for call distribution by hour
        filtered_df_sampled = filtered_df.sample(1000)  # Sampling data for better performance
        sns.boxplot(x=filtered_df_sampled["Hour"])
        st.pyplot(fig6)

        call_by_day = filtered_df.groupby("Day")["Hour"].count()  # Call distribution by day
        fig8 = px.line(call_by_day, x=call_by_day.index, y=call_by_day.values, title="📅 Call Distribution by Day of the Week", labels={"x": "Day", "y": "Number of Calls"})
        st.plotly_chart(fig8, use_container_width=True)

        fig9 = px.histogram(filtered_df, x="Hour", title="📊 Call Distribution by Hour of the Day")  # Calls by hour
        st.plotly_chart(fig9, use_container_width=True)

# *Tab 2: Map View*
with tab2:
    st.subheader("📍 Calls Location Map")  # Map of call locations
    filtered_df_temp = filtered_df.rename(columns={"latitude": "latitude", "longitude": "longitude"})
    st.map(filtered_df_temp[["latitude", "longitude"]].dropna())  # Display the map with dropna

# *Tab 3: Descriptive Stats*
with tab3:
    st.subheader("📊 Descriptive Statistics")
    st.markdown("### Descriptive Statistics for Numeric Columns")  # Descriptive stats for numeric data
    st.write(filtered_df.describe())

    st.markdown("### Descriptive Statistics for Categorical Columns")  # Descriptive stats for categorical data
    categorical_stats = filtered_df.select_dtypes(include=['object']).nunique()
    st.write(categorical_stats)

# ---- DATA TABLE ----
st.markdown("### 📝 Dataset Preview")  # Displaying dataset preview
st.dataframe(filtered_df.head(100))  # Showing the first 100 rows
