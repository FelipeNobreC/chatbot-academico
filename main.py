from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import chat

app = FastAPI(title="Chatbot Acadêmico Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat", tags=["chat"])