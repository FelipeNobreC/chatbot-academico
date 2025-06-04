# Padrão Command para encapsular ações
class Command:
    def execute(self, *args, **kwargs):
        pass

class HelpCommand(Command):
    def execute(self, *args, **kwargs):
        return 'Este é o chatbot acadêmico. Faça perguntas ou use comandos.'

class EchoCommand(Command):
    def execute(self, message, *args, **kwargs):
        return f'Você disse: {message}'

class UnknownCommand(Command):
    def execute(self, *args, **kwargs):
        return 'Desculpe, não reconheço esse comando.'