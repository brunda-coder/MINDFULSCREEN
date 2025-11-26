#!/usr/bin/env python3
"""
MINDFULSCREEN — Etherea Living OS (MVP)
main.py: starts a FastAPI application exposing a tiny REST + WebSocket surface,
loads config and pluggable modules (ai_engine, voice_system, chat_system).
"""

import asyncio
import json
import logging
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import uvicorn

# local imports (modules are simple stubs in their folders)
from core import manager
from ai_engine import ai
from voice_system import tts, stt
from chat_system import chat

CONFIG_PATH = Path(__file__).parent / "app_config.json"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("etherea")

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf8") as f:
            return json.load(f)
    logger.warning("config not found — using defaults")
    return {}

app = FastAPI(title="Etherea Living OS — MINDFULSCREEN (MVP)")
config = load_config()

# simple health endpoint
@app.get("/health")
async def health():
    return {"status": "ok", "service": "etherea", "version": config.get("version", "0.0.1")}

# info about enabled modules
@app.get("/info")
async def info():
    return {
        "modules": ["core.manager", "ai_engine.ai", "voice_system.stt/tts", "chat_system.chat"],
        "config": config
    }

# simple REST route to run an AI prompt
@app.post("/ai/prompt")
async def run_prompt(payload: dict):
    prompt = payload.get("prompt", "")
    if not prompt:
        return JSONResponse({"error": "prompt missing"}, status_code=400)
    # run ai engine (sync or async depending on stub)
    response = await ai.handle_prompt(prompt, config=config)
    return {"prompt": prompt, "response": response}

# websocket chat endpoint — echo + forward to ai engine
@app.websocket("/ws/chat")
async def websocket_chat(ws: WebSocket):
    await ws.accept()
    try:
        await ws.send_json({"system": "connected"})
        while True:
            data = await ws.receive_json()
            user_msg = data.get("message", "")
            if not user_msg:
                await ws.send_json({"error": "no message field"})
                continue
            # stream/compute response from ai engine
            resp = await ai.handle_prompt(user_msg, config=config)
            await ws.send_json({"reply": resp})
    except WebSocketDisconnect:
        logger.info("websocket disconnected")

if __name__ == "__main__":
    # perform lightweight module initialization
    manager.initialize(config)
    # run uvicorn programmatically for convenience
    uvicorn.run("main:app", host=config.get("host", "127.0.0.1"), port=config.get("port", 8000), reload=True)
