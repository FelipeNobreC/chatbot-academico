from fastapi import APIRouter
from backend.llama_handler import LlamaModelHandler
from backend.patterns.chain import CommandHandler, ModelHandler, FilterHandler
from backend.patterns.command import HelpCommand, EchoCommand, UnknownCommand
from backend.patterns.observer import user_created_event

router = APIRouter()

# Instancia o modelo de linguagem
llama_handler = LlamaModelHandler()

# Configura os comandos disponíveis
commands = {
    'help': HelpCommand(),
    'echo': EchoCommand(),
    'unknown': UnknownCommand()
}

# Configura a cadeia de responsabilidade
command_handler = CommandHandler(commands)
filter_handler = FilterHandler()
model_handler = ModelHandler(llama_handler)

command_handler.set_next(filter_handler).set_next(model_handler)

@router.post("/send")
def send_message(request: dict):
    # Cria evento de observação (notificando criação de usuário)
    user_created_event.notify({"nome": "Usuário Teste", "curso": "Engenharia"})

    # Processa a pergunta usando a cadeia
    resposta = command_handler.handle(request['question'])

    return {"question": request['question'], "answer": resposta}