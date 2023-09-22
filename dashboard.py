import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

dashboardDf = pd.read_csv("dashboard.csv")

def casualDashboard(df):
    st.subheader('Casual Users Rental')
 
    totalRentals = df.casual.sum()
    st.metric("Total Rental", value = totalRentals)
        
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df["dteday"],
        df["casual"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)
    
def registeredDashboard(df):
    st.subheader('Registered Users Rental')
 
    totalRentals = df.registered.sum()
    st.metric("Total Rental", value = totalRentals)
        
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df["dteday"],
        df["registered"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

minDate = dashboardDf["dteday"].min()
maxDate = dashboardDf["dteday"].max()

minDate = datetime.strptime(minDate, '%Y-%m-%d')
maxDate = datetime.strptime(maxDate, '%Y-%m-%d')

with st.sidebar:
    st.title("Welcome to my Dashboard")
    st.image("logo.jpg")
    startDate, endDate = st.date_input(
        label = 'Time Range',
        min_value = minDate,
        max_value = maxDate,
        value = [minDate, maxDate]
    )

xDf = dashboardDf[(dashboardDf["dteday"] >= str(startDate)) & (dashboardDf["dteday"] <= str(endDate))]

st.header('Bike Rental Dashboard')
casualDashboard(xDf)
registeredDashboard(xDf)