import requests
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv("ChatGTPAPIKey")

# Vérifier que la clé API est présente
if not api_key:
    print("API key is missing. Please check your .env file.")
    exit()

# Paramètres par défaut
model = "gpt-3.5-turbo"  # Utiliser un modèle valide comme gpt-3.5-turbo ou gpt-4 si vous y avez accès
prompt = "Here the prompt to send to chatgpt"
max_tokens = 100  # Vous pouvez ajuster ce nombre de tokens

# Fonction pour modifier dynamiquement les paramètres
def set_parameters(model_choice=None, prompt_text=None, max_tokens_value=None):
    global model, prompt, max_tokens
    if model_choice:
        model = model_choice
    if prompt_text:
        prompt = prompt_text
    if max_tokens_value:
        max_tokens = max_tokens_value

# Exemple de modification dynamique des paramètres
set_parameters(model_choice="gpt-3.5-turbo", prompt_text="What is the weather today?", max_tokens_value=50)

# En-têtes HTTP pour la requête
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Structure des messages pour l'API
parameters = {
    "model": model,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    "max_tokens": max_tokens
}

# Effectuer la requête POST à l'API OpenAI
response = requests.post(f"https://api.openai.com/v1/chat/completions", headers=headers, json=parameters)

# Vérifier la réponse de l'API
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Error {response.status_code}: {response.text}")
