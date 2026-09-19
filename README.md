# sprint7git
Este es un repositorio dedicado al proyecto de Sprint 7: Herramientas de desarrollo de software

# Análisis de anuncios de venta de coches

Este proyecto es parte del Sprint 7 Herramientas de desarrollo de software, consiste en una aplicación web hecha con Streamlit para explorar un conjunto de datos de anuncios de venta de coches en Estados Unidos (`vehicles_us.csv`).

## ¿Para qué sirve la aplicación?

Permite explorar visualmente los datos de forma interactiva, sin necesidad de escribir código.

## Funcionalidad

- **Histograma del odómetro:** muestra cómo se distribuye el kilometraje de los vehículos anunciados.
- **Gráfico de dispersión precio vs. odómetro:** permite ver la relación entre el recorrido y el precio de los vehículos.

Los gráficos son interactivos (zoom, desplazamiento y detalle al pasar el cursor) y se construyen con Plotly.

## Estructura del proyecto

- `app.py`: aplicación web de Streamlit.
- `notebooks/EDA.ipynb`: análisis exploratorio de datos.
- `vehicles_us.csv`: conjunto de datos.
- `requirements.txt`: dependencias (pandas, plotly, streamlit).

## Cómo ejecutar la aplicación

1. Crea y activa un entorno virtual.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta: `streamlit run app.py`

##Aplicación en línea
https://sprint7git.onrender.com
