#!/usr/bin/env python3
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Obtener la API key desde la variable de entorno
API_KEY = os.getenv('GOOGLE_API_KEY')

# Instanciar el modelo de Google Generative AI
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=API_KEY,  # 🔑 Aquí va 'api_key', no 'google_api_key'
    temperature=0,
    streaming=True,  # ⚡ habilita streaming
    callbacks=[StreamingStdOutCallbackHandler()]
)
