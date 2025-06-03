from backend.patterns.observer import user_created_event

def log_new_user(user):
    print(f"[Observer] Novo usuário registrado: {user.nome}, Curso: {user.curso}")

# Registra o observador
user_created_event.register(log_new_user)