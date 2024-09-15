import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st   
import plotly.express as px

data = pd.read_csv('./vehicles_us.csv')
data.fillna(0, inplace = True)
st.header('Creacion de graficos')
hist_button = st.button('Construir histograma') 
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: 
   
    st.write(hist_button)       
if hist_button:
    

    st.write('Creación de un histograma')
            
    fig = px.histogram(data , x="odometer")

    st.plotly_chart(fig)
build_scatter = st.checkbox('Construir un grafico de dispersion')

if build_scatter: 
   
    st.write('Construir un grafico de dispersion')

scatter_button = st.button('construir grafico de dispersion')
if scatter_button: 

        st.write('Creación de un grafico de dispersion') 
                                   
        fig2 = px.scatter(data , x="odometer", y="price") 
        
        st.plotly_chart(fig2)