# 🦜🔗 Mi Primera App con LangChain y GPT-4o-mini

🌐 **Demo en vivo:** [https://taller-langchain.streamlit.app](https://taller-langchain.streamlit.app)

Aplicación web construida con **Streamlit**, **LangChain** y **OpenAI (`gpt-4o-mini`)**, basada en el tutorial oficial de Streamlit (*Build an LLM-powered app in 18 lines of code*).

## 🚀 Ejecución en local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/HernanLopez1/Langchain-Streamlit-OpenAI.git
   cd Langchain-Streamlit-OpenAI
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar la variable de entorno creando un archivo `.env` a partir de `.env.example`:
   ```env
   OPENAI_API_KEY=sk-proj-...
   ```

4. Ejecutar la aplicación:
   ```bash
   streamlit run streamlit_app.py
   ```

## ☁️ Despliegue en Streamlit Community Cloud

En **Advanced settings -> Secrets** dentro de Streamlit Community Cloud, agrega tu clave:

```toml
OPENAI_API_KEY = "sk-proj-..."
```
