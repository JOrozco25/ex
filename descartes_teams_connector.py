import os
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TEAMS_WEBHOOK_URL = os.getenv('TEAMS_WEBHOOK_URL')


def get_descartes_update():
    """Simulate retrieval of an update from Descartes system."""
    # Placeholder: in a real scenario, fetch data from Descartes API or database
    return "Estado de envío actualizado en Descartes"


def ask_chatgpt(prompt: str) -> str:
    """Send a prompt to OpenAI's ChatGPT API and return the response text."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def send_to_teams(message: str):
    """Post a message to Microsoft Teams using an incoming webhook."""
    if not TEAMS_WEBHOOK_URL:
        raise ValueError("TEAMS_WEBHOOK_URL environment variable not set")

    payload = {"text": message}
    resp = requests.post(TEAMS_WEBHOOK_URL, json=payload)
    resp.raise_for_status()


def main():
    desc = get_descartes_update()
    prompt = f"Genera un breve resumen para Teams basado en: {desc}"
    gpt_response = ask_chatgpt(prompt)
    send_to_teams(gpt_response)


if __name__ == "__main__":
    main()
