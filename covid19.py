import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Set page config
st.set_page_config(page_title="Covid-19 Pandemic Dashboard", layout="wide")

# Title
st.title("💉 Covid-19 Pandemic Dashboard")

# Load & preprocess data
df1 = pd.read_csv('day_wise.csv')
df2 = pd.read_csv('country_wise_latest.csv')

# KPI Metrics
total_deaths = df1['Deaths'].sum()
total_cases = df1['Confirmed'].sum()
total_recovered = df1['Recovered'].sum()

# Sidebar
chart_type = st.sidebar.radio("📊 Select Visualization", 
                              ["📄 Show Dataset 1", "📄 Show Dataset 2","📌 KPI Metrics", "📍 Bar Chart: Total Cases by Country", 
                               "📈 Line Chart: Daily Cases Trend", 
                               "🥧 Pie Chart: Recovery vs Death Rate"])

# Show dataset
if chart_type == "📄 Show Dataset 1":
    st.subheader("🧾 Day Wise Cases Data")
    st.dataframe(df1)
elif chart_type == "📄 Show Dataset 2":
    st.subheader("🧾 Country Wise Cases Data")
    st.dataframe(df2)

# KPI Metrics
elif chart_type == "📌 KPI Metrics":
    st.subheader("📊 Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric(" Total Deaths", f"{total_deaths:,.0f}")
    col2.metric(" Total Recovered", f"{total_recovered:,.0f}")
    col3.metric(" Total cases", f"{total_cases:,.0f}")

# Bar Chart
elif chart_type == "📍 Bar Chart: Total Cases by Country":
    st.subheader("📍 Total Cases by Country")
    fig = px.bar(df2, y="Confirmed", x="Country/Region", title="Total Cases by Country")
    st.plotly_chart(fig, use_container_width=True)
    # st.plotly_chart(fig, config=config)
    # fig.show()
    
   

# Line Chart
elif chart_type == "📈 Line Chart: Daily Cases Trend":
    st.subheader("📈 Daily Cases Trend")
    fig = px.line(df1, x="Date", y="Confirmed", title="Daily Cases Over Time")
    fig.add_scatter(x=df1['Date'], y=df1['Active'], mode='lines', name='Active Cases')
    fig.add_scatter(x=df1['Date'], y=df1['Deaths'], mode='lines', name='Deaths')
    fig.add_scatter(x=df1['Date'], y=df1['Recovered'], mode='lines', name='Recovered')
    st.plotly_chart(fig, use_container_width=True)
    # fig.show()

# Pie Chart
elif chart_type == "🥧 Pie Chart: Recovery vs Death Rate":
    st.subheader("🥧 Overall Recovery vs Death Rate")
    # Calculate total recovered and total deaths
    total_recovered = df2['Recovered'].sum()
    total_deaths = df2['Deaths'].sum()
    
    # Create labels and sizes for the pie chart
    labels = ['Recovered', 'Deaths']
    sizes = [total_recovered, total_deaths]
    
    data = {'Category': ['Recovered', 'Deaths'],
            'Count': [total_recovered, total_deaths]}
    pie_df = pd.DataFrame(data)
    # Create the interactive pie chart
    fig = px.pie(pie_df, values='Count', names='Category', title='Overall Recovery vs Death Rate')
    st.plotly_chart(fig, theme=None)