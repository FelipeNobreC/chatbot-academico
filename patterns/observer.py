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