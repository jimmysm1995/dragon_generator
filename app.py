import streamlit as st
import requests

# URL de la API de Stable Diffusion
api_url = "http://127.0.0.1:7860/sdapi/v1/txt2img/"

# Título de la aplicación
st.title("Generador de Imágenes de dragones")

# Entrada de selección para el prompt
color = st.selectbox("Selecciona el color del dragón:", ["Rojo", "Verde", "Azul"])
size = st.selectbox("Selecciona el tamaño del dragón:", ["Pequeño", "Mediano", "Grande"])
background = st.selectbox("Selecciona el fondo del dragón:", ["Bosque", "Montaña", "Cielo"])

prompt = f"Un dragón de color {color} de tamaño {size} en un fondo {background}"

# Parámetros adicionales
steps = st.slider("Número de pasos:", min_value=1, max_value=100, value=50)
width = st.slider("Ancho de la imagen:", min_value=64, max_value=1024, value=512)
height = st.slider("Alto de la imagen:", min_value=64, max_value=1024, value=512)
bath_size = st.slider("Numero de imágenes:", min_value=1, max_value=5, value=1)

# Botón para generar la imagen
if st.button("Generar Imagen"):
    # Datos de la solicitud
    data = {
        "prompt": prompt,
        "steps": steps,
        #"width": width,
        #"height": height,
        #"batch": bath_size
    }

    # Hacer la solicitud POST a la API
    response = requests.post(api_url, json=data)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Mostrar la imagen generada
        st.image(response.content, caption="Imagen generada")
    else:
        st.error(f"Error: {response.status_code}")
        st.json(response.json())