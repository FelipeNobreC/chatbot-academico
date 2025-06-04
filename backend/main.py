from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import chat

# Instância do FastAPI
app = FastAPI(title="Chatbot Acadêmico Backend")

# Configuração do CORS para permitir que o frontend se conecte a qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Inclui as rotas do chatbot
app.include_router(chat.router, prefix="/chat", tags=["chat"])