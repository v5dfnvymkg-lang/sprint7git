import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de anuncios de venta de coches')

# Casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del odómetro')

    st.plotly_chart(fig, width='stretch')

if build_scatter:
    st.write('Construir un gráfico de dispersión: precio vs. odómetro')

    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Precio vs. odómetro',
                      xaxis_title='Odómetro',
                      yaxis_title='Precio')

    st.plotly_chart(fig, width='stretch')