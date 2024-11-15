import google.generativeai as genai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
API_KEY = os.getenv("API_KEY")

# Configurer l'API Generative AI
genai.configure(api_key=API_KEY)

# Utiliser le modèle Generative AI
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Translate this text to French: Hello, how are you?")
print(response.text)