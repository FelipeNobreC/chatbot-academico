# Chatbot Acadêmico - Backend com Padrões Comportamentais

Projeto backend completo com FastAPI que implementa um chatbot acadêmico usando o modelo TeenyTinyLlama-460m local, integrando os padrões de projeto comportamentais:

- Chain of Responsibility
- Observer
- Command

---

## Pré-requisitos

- Python 3.9 ou superior
- Pip instalado
- Modelo TeenyTinyLlama-460m `.bin` baixado (link abaixo)
- Windows/Linux/Mac com CPU compatível
- Internet para baixar dependências

---

## Passo 1: Clonar ou baixar o projeto

Baixe o arquivo ZIP e extraia em sua máquina.

---

## Passo 2: Instalar dependências

Abra terminal/prompt na pasta do projeto e execute:

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] pydantic llama-cpp-python aiofiles
```

---

## Passo 3: Baixar o modelo TeenyTinyLlama-460m

Baixe o modelo `.bin` em:

https://huggingface.co/nicholasKluge/TeenyTinyLlama-460m

Coloque o arquivo baixado dentro da pasta:

```
backend/models/teenytinyllama-460m.bin
```

---

## Passo 4: Rodar a aplicação

Na pasta raiz do projeto, execute o comando para iniciar o backend:

```bash
uvicorn backend.main:app --reload
```

O servidor iniciará em:

```
http://localhost:8000
```

---

## Passo 5: Usar a API

- Endpoints principais:

  - POST `/auth/register` - registra novo usuário
  - POST `/auth/login` - faz login e retorna token JWT
  - POST `/chat/send` - envia pergunta ao chatbot (token Bearer necessário)
  - GET `/admin/stats` - estatísticas (somente admin)
  - GET `/admin/export` - exporta histórico CSV (somente admin)

---

## Padrões implementados

- **Chain of Responsibility:** tratamento das perguntas por handlers (comando, filtro, modelo)
- **Observer:** notificação desacoplada para eventos (ex: usuário criado)
- **Command:** comandos encapsulados para respostas pré-definidas (`/help`, `/echo`)

---

## Observações

- Para testes, registre um usuário e faça login para obter o token JWT.
- Use comandos iniciados com `/` para testar comandos, ex: `/help` ou `/echo ola`.
- O usuário com nome `admin` tem acesso ao painel administrativo.
- Logs de eventos observados aparecerão no console (ex: cadastro de usuário).

---

## Dúvidas ou suporte

Me avise que te ajudo!

---