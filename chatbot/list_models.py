import google.generativeai as genai
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Listar todos los modelos disponibles
models = genai.list_models()
for m in models:
    print(m)
