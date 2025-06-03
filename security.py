# Funções de segurança, hashing de senha, criação e verificação de token JWT

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User

# Chave secreta para assinatura JWT (em produção, manter segredo e seguro)
SECRET_KEY = "supersecretkey1234567890"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # Token válido por 7 dias

# Contexto para hashing de senha com bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 com password flow para autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Verifica se senha em texto plano bate com hash
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Gera hash para a senha
def get_password_hash(password):
    return pwd_context.hash(password)

# Cria token JWT com dados e expiração
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Recupera usuário atual a partir do token JWT
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        nome: str = payload.get("sub")
        if nome is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.nome == nome).first()
    if user is None:
        raise credentials_exception
    return user

# Função que garante acesso só para admin (usuário com nome 'admin')
def get_current_admin(current_user: User = Depends(get_current_user)):
    if current_user.nome != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado ao painel administrativo")
    return current_user
