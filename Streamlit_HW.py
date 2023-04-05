import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime
import plotly.express as px

# Post 2 links. One to your GitHub repository and one to your published Streamlit app.  
# This is an interactive application that you create preferably using your midterm data, but if that is not possible use any data of your choice.  
# Create at least one visual that has two interactions that the user can change.

df = pd.read_csv("ODs.csv")

st.set_page_config(layout = "wide")
st.header("Overdose Deaths")

page = st.sidebar.selectbox("Select Scope",
  ["State", "Regional"])

if page == "State":
  
## States
  state_list = df["State"].unique()
  state = st.selectbox("Select a State:",state_list)
  col1, col2 = st.columns(2)
  fig = px.line(df[df["State"] == state], 
    x = "Year", y = "Opioid_Overdose_Death_Rate",title = "Opioid Overdose Deaths")
 
  col1.plotly_chart(fig,use_container_width = True)
  fig = px.line(df[df["State"] == state], 
    x = "Year", y = "All_Drug_Overdose_Death_Rate",title = "All Drug Overdose Deaths")
  
  col2.plotly_chart(fig,use_container_width = True)
else:
  
## Regions
  region_list = df["Region"].unique()
 
  region = st.selectbox("Select a Region:",region_list)
  col1,col2 = st.columns(2)
  fig = px.line(df[df['Region'] == region], 
    x = "Year", y = "Opioid_Overdose_Death_Rate",
    title = "Opioid Overdose Deaths",color = "Region")
  
  col1.plotly_chart(fig)
  fig = px.line(df[df["Region"] == region], x = "Year", y = "All_Drug_Overdose_Death_Rate",
  title = "All Drug Overdose Deaths",color = "Region")
  
  col2.plotly_chart(fig, use_container_width = True)
