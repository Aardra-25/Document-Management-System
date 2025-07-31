import google.generativeai as genai
from core.config_llm import google_genai_config 

# Set your API key here
genai.configure(api_key=google_genai_config.google_genai_api_key)

def ask_model(question):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(question)
    return response.text