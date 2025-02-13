# Generador de Imágenes de Dragones

Este proyecto es una aplicación de Streamlit que genera imágenes de dragones basadas en atributos seleccionados por el usuario, como color, tamaño y fondo. La aplicación interactúa con una API de Stable Diffusion para generar las imágenes.

## Características

- Selecciona el color, tamaño y fondo del dragón.
- Ajusta parámetros adicionales como el número de pasos, ancho y alto de la imagen.
- Genera y muestra la imagen del dragón basada en los atributos seleccionados.

## Herramientas y Tecnologías Utilizadas

- **Python**: El lenguaje de programación principal utilizado para la aplicación.
- **Streamlit**: Un framework para crear aplicaciones web interactivas en Python.
- **Requests**: Una biblioteca para hacer solicitudes HTTP e interactuar con la API de Stable Diffusion.
- **Docker**: Utilizado para contenerizar la aplicación y facilitar su despliegue.

## Instalación

1. **Clonar el repositorio**:
    ```sh
    git clone https://github.com/yourusername/dragon-image-generator.git
    cd dragon-image-generator
    ```

2. **Construir y ejecutar el contenedor Docker**:
    ```sh
    docker-compose up --build
    ```

3. **Acceder a la aplicación**:
    Abre tu navegador web y ve a `http://localhost:8501`.

## Uso

1. **Selecciona los atributos**:
    - Elige el color del dragón.
    - Elige el tamaño del dragón.
    - Elige el fondo para el dragón.

2. **Ajusta los parámetros adicionales**:
    - Establece el número de pasos para la generación de la imagen.
    - Establece el ancho y alto de la imagen.
    - Establece el número de imágenes a generar.

3. **Genera la imagen**:
    - Haz clic en el botón "Generar Imagen" para generar y mostrar la imagen del dragón.

## Explicación del Código

- **`app.py`**: El archivo principal de la aplicación que configura la interfaz de Streamlit y maneja la entrada del usuario para generar la imagen del dragón.
- **`Dockerfile`**: Define la imagen Docker para la aplicación, incluyendo la instalación de dependencias.
- **`docker-compose.yml`**: Configura los servicios Docker, incluyendo el servicio de la aplicación y los mapeos de puertos.
- **`requirements.txt`**: Lista las dependencias de Python requeridas para la aplicación.

## Solución de Problemas

Si encuentras un `ConnectionError` al intentar generar una imagen, asegúrate de que el servidor de la API de Stable Diffusion esté en funcionamiento y accesible en `http://127.0.0.1:7860`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
