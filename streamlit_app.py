import os
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env
load_dotenv()

st.title('🦜🔗 Mi Primera App con LangChain y GPT-4o-mini')

# 2. Obtener la API key de las variables de entorno (local .env o Streamlit Cloud Secrets)
openai_api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", None)

def generate_response(input_text):
    # Usamos la clase ChatOpenAI y el modelo gpt-4o-mini
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=openai_api_key)
    
    # Invocamos el modelo y extraemos el contenido del mensaje
    response = llm.invoke(input_text)
    st.info(response.content)

with st.form('my_form'):
    text = st.text_area('Ingresa tu texto:', '¿Cuáles son 3 consejos clave para aprender a programar?')
    submitted = st.form_submit_button('Enviar')
    
    # 3. Validar que la llave exista en el .env antes de ejecutar
    if not openai_api_key or not openai_api_key.startswith('sk-'):
        st.warning('¡No se encontró una OpenAI API key válida en el archivo .env!', icon='⚠')
    elif submitted:
        generate_response(text)