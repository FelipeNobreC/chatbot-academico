# Padrão Observer para notificar eventos
class Event:
    def __init__(self):
        self.__observers = []

    def register(self, observer_func):
        self.__observers.append(observer_func)

    def notify(self, *args, **kwargs):
        for observer in self.__observers:
            observer(*args, **kwargs)

# Instância global para eventos de usuário criado
user_created_event = Event()

# Exemplo de observador simples: logar criação de usuário
def log_new_user(user):
    print(f"[Observer] Novo usuário registrado: {user.nome}, Curso: {user.curso}")

# Registra o observador
user_created_event.register(log_new_user)