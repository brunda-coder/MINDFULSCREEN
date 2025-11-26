# MINDFULSCREEN
“An AI-powered digital wellness tracker that monitors screen time and reminds you to take breaks mindfully.”

# MINDFULSCREEN — Etherea Living OS (MVP)

This repository contains a minimal, modular MVP for Etherea Living OS (MINDFULSCREEN).

## Structure
- `core/` — application bootstrap + module manager
- `ai_engine/` — AI prompt handler (stubbed)
- `voice_system/` — speech-to-text and text-to-speech stubs
- `chat_system/` — simple chat logic and websocket helpers
- `frontend/` — (optional) UI or web client
- `main.py` — FastAPI app
- `launcher.py` — tiny CLI
- `app_config.json` — config
- `requirements.txt` — Python deps

## Quick start (dev)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python launcher.py run
# then open http://127.0.0.1:8000/health

