# Conector Descartes a ChatGPT Teams

Este repositorio contiene un ejemplo sencillo (MCP) para conectar el sistema **Descartes** con un conector de ChatGPT en Microsoft Teams.

## Requisitos

- Python 3.8+
- Las dependencias listadas en `requirements.txt`
- Variables de entorno:
  - `OPENAI_API_KEY` con la clave de acceso a OpenAI
  - `TEAMS_WEBHOOK_URL` con la URL del webhook entrante de Teams

## Uso

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Copiar `.env.example` a `.env` y completar tus credenciales:
   ```bash
   cp .env.example .env
   # editar .env con OPENAI_API_KEY y TEAMS_WEBHOOK_URL
   ```
3. Ejecutar el conector:
   ```bash
   python descartes_teams_connector.py
   ```

El script recupera información simulada de Descartes, genera un resumen con ChatGPT y lo publica en el canal de Teams configurado.
