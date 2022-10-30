#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:13:04 2022

@author: ginger-pipeline
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import cv2 as cv
import tempfile
import numpy as np
import pandas as pd
import datetime


# Create a title for our web page
st.title("Track Tracker")
st.write("Extend your running statistics and make your performance more compareable!")

df = pd.read_csv("running_summary.csv")
df.dropna(inplace=True)

#Total Distance
Total_distance = round(df['total_distance'].sum(),2)
last_row_df = df.iloc[-1:]

delta_distance = round(last_row_df['total_distance'].sum(),2)

#Total Time
Total_time = df['total_time'].sum()
#last_row_df = df.iloc[-1:]

delta_time = last_row_df['total_time'].sum()
delta_hour = Total_time/60

result_time = str(datetime.timedelta(minutes=delta_time))
float_time = Total_time  # in minutes
hours, seconds = divmod(float_time * 60, 3600)  # split to hours and seconds
minutes, seconds = divmod(seconds, 60)  # split the seconds to minutes and seconds
result = "{:02.0f}:{:02.0f}:{:02.0f}".format(hours, minutes, seconds)

#DTR
dtr = round(df['ATR'].sum()/len(df['ATR']),2)
dtr_delta = last_row_df['ATR'].sum()

#FTR
ftr = round(df['FTR'].sum()/len(df['FTR']),2)
ftr_delta = last_row_df['FTR'].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Distance", Total_distance, delta_distance, help="This is the total distance run")
col2.metric("Total Time", result, result_time, help="This is the total distance run")
col3.metric("Total Asphalt Track Ratio", dtr, dtr_delta, help="This is your average Asphalt Track Ratio" )
col4.metric("Total Forest Track Ratio", ftr, ftr_delta, help="This is your average Field Track Ratio")

st.subheader('Distance per track on your last run')
afield_distance_last = round(last_row_df['asphalt_field_distance'].sum(),2)
aforest_distance_last = round(last_row_df['asphalt_forest_distance'].sum(),2)
dfield_distance_last = round(last_row_df['dirt_field_distance'].sum(),2)
dforest_distance_last = round(last_row_df['dirt_forest_distance'].sum(),2)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Asphalt Field Distance", afield_distance_last)
col2.metric("Total Asphalt Forest Distance", aforest_distance_last)
col3.metric("Total Dirt Field Distance", dfield_distance_last)
col4.metric("Total Dirt Forest Distance", dforest_distance_last)

labels = 'Asphalt Field Track ', 'Asphalt Forest Track', 'Dirt Field Track', 'Dirt Forest Track'

size_of_groups = [afield_distance_last, aforest_distance_last, dfield_distance_last, dforest_distance_last]
fig7, ax7 = plt.subplots()
ax7 = plt.pie(size_of_groups, labels=labels, autopct='%1.1f%%')
st.pyplot(fig7)


# Distance Figure
st.subheader('Total distance run on each track')
afield_distance = round(df['asphalt_field_distance'].sum(),2)
aforest_distance = round(df['asphalt_forest_distance'].sum(),2)
dfield_distance = round(df['dirt_field_distance'].sum(),2)
dforest_distance = round(df['dirt_forest_distance'].sum(),2)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Asphalt Field Distance", afield_distance)
col2.metric("Total Asphalt Forest Distance", aforest_distance)
col3.metric("Total Dirt Field Distance", dfield_distance)
col4.metric("Total Dirt Forest Distance", dforest_distance)

afield_distance = df['asphalt_field_distance'].sum()
aforest_distance = df['asphalt_forest_distance'].sum()
dfield_distance = df['dirt_field_distance'].sum()
dforest_distance =df['dirt_forest_distance'].sum()

labels = 'Asphalt Track Field', 'Asphalt Track Forest', 'Dirt Track Field', 'Dirt Track Forest'

size_of_groups = [afield_distance, aforest_distance, dfield_distance, dforest_distance]
fig2, ax4 = plt.subplots()
ax4 = plt.pie(size_of_groups, labels=labels, autopct='%1.1f%%')
st.pyplot(fig2)

st.write(df.head(10))
