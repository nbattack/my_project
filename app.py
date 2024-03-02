import streamlit as st 
import pandas as pd 
import plotly.express as px 
car_data = pd.read_csv("/Users/Daye Seijas/my_project/vehicles_us.csv")
#car_data.info()
st.header('Información de Venta de Vehiculos')

button=st.button('Histograma')
if button:
    st.write('Histograma de conjunto de datos de anuncios de ventas de autos')
    fig=px.histogram(car_data,x='odometer')
    st.plotly_chart(fig, use_container_width=True)

button_2=st.button('Dispersión')
if button_2:
    st.write('Diagrama de dispersión de datos')
    fig_2=px.scatter(car_data,x='odometer')
    st.plotly_chart(fig_2, use_container_width=True)

#Casillas de verificación
build_histogram = st.checkbox('Contruyendo histograma')
if build_histogram:
    st.write('Histograma de datos de anuncios de ventas de autos')
    fig=px.histogram(car_data,x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construyendo dispersión')
if build_scatter:
    st.write('Diagrama de dispersión de datos')
    fig_2=px.scatter(car_data, x='odometer')
    st.plotly_chart(fig_2, use_container_width=True)