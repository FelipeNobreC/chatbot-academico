from fastapi import APIRouter
from backend.llama_handler import LlamaModelHandler

# Importa padrões
from backend.patterns.chain import CommandHandler, ModelHandler
from backend.patterns.command import HelpCommand, EchoCommand, UnknownCommand

router = APIRouter()

llama_handler = LlamaModelHandler("models/teenytinyllama-460m.bin")

# Configura os comandos disponíveis
commands = {
    'help': HelpCommand(),
    'echo': EchoCommand(),
    'unknown': UnknownCommand()
}

# Monta a cadeia de responsabilidade
command_handler = CommandHandler(commands)
model_handler = ModelHandler(llama_handler)

command_handler.set_next(model_handler)

@router.post("/send")
def send_message(request: dict):
    # Processa a pergunta usando a cadeia
    resposta = command_handler.handle(request['question'])

    return {"question": request['question'], "answer": resposta}