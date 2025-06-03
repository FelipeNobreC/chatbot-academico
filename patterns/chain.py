class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class CommandHandler(Handler):
    def __init__(self, commands):
        super().__init__()
        self.commands = commands  # dict of command name -> Command instance

    def handle(self, request):
        text = request.strip()
        if text.startswith('/'):
            cmd_name = text.split()[0][1:].lower()
            cmd = self.commands.get(cmd_name, self.commands.get('unknown'))
            return cmd.execute(text)
        else:
            return super().handle(request)

class FilterHandler(Handler):
    def handle(self, request):
        # Exemplo simples de filtro: bloquear pergunta vazia
        if not request.strip():
            return 'Pergunta vazia não é permitida.'
        return super().handle(request)

class ModelHandler(Handler):
    def __init__(self, llama_handler):
        super().__init__()
        self.llama_handler = llama_handler

    def handle(self, request):
        return self.llama_handler.ask(request)