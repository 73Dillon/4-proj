#load in packages
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px
import streamlit as st

#read in csv
df = pd.read_csv('c:/Users/dillo/Documents/Triple10/Sprint-4/4-proj/new_vehicles_us.csv')

#title
st.title('Car Sales Listings in the U.S.')

#header and data viewer
st.header('Data Viewer')
st.dataframe(df)

#histogram of type by car brand
fig = px.histogram(df, x='type', color='brand', labels={'count': 'Listings'}, title='Vehile Types by Brand')
st.plotly_chart(fig, use_container_width=True)

#histogram of model year by condition
fig1 = px.histogram(df, x='model_year', color='condition', title='Vehicle Condition by Model Year')
st.plotly_chart(fig1, use_container_width=True)

#header for car price compare chart
st.header('Compare Average Prices of Popular Car Types Between Brands')

#first selectbox of car brands
option = st.selectbox("Brand 1", options=df['brand'].unique(),)
#second selectbox of car brands
option1 = st.selectbox("Brand 2", options=df['brand'].unique(),)

#histogram that compares average prices between popular types of cars made by two brands
brands = [option, option1]
types = ['sedan', 'truck', 'SUV', 'hatchback']
df2 = df[df['brand'].isin(brands) & (df['type'].isin(types))]
fig2 = px.histogram(df2, x='type', y='price', color='brand', histfunc='avg', barmode='group')
st.plotly_chart(fig2, use_container_width=True)

#header for scatter of car model price v days_listed for select brand
st.header('Model Price vs Days Listed by Brand')

#selectbox for brand
scatter_select = st.selectbox("Brand", options=df['brand'].unique(),)

#scatter of car model price v days_listed for select brand
df1 = df[df['brand']==scatter_select]
fig3 = px.scatter(df1, x='price', y='days_listed', color='car_model', opacity=.8)
st.plotly_chart(fig3, use_container_width=True)
