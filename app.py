import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st   
import plotly.express as px

data = pd.read_csv('./vehicles_us.csv')
data.fillna(0, inplace = True)
hist_button = st.button('Construir histograma') 
        
if hist_button:
    

    st.write('Creación de un histograma')
            
    fig = px.histogram(data , x="odometer")

    st.plotly_chart(fig)
  
