import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st   
import plotly.express as px

df = pd.read_csv('./vehicles_us.csv')

df.fillna(0,inplace=True)


boton_hist = st.button('crear histograma') 

if boton_hist:
    st.write('Creación de un histograma para el conjunto de datos')

    fig = px.histogram(df, x="odometer")

    st.plotly_chart(fig, use_container_width=True)