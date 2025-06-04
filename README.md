# Chatbot Acadêmico - Backend com Hugging Face

Este projeto é um chatbot acadêmico simples, onde qualquer pessoa pode interagir com o sistema para obter respostas. O backend usa **FastAPI** e **transformers** do Hugging Face para gerar respostas com o modelo **TeenyTinyLlama-460m**.

---

## Como rodar o projeto:

### Passo 1: Instalar as dependências

No terminal, dentro da pasta do projeto, execute o seguinte comando para instalar as dependências:
```bash
pip install transformers fastapi uvicorn torch
```

### Passo 2: Rodar o servidor

Execute o comando abaixo para rodar o servidor FastAPI:
```bash
uvicorn backend.main:app --reload
```

O backend estará rodando em `http://localhost:8000`.

### Passo 3: Interagir com o chatbot

Acesse a rota `/chat/send` para interagir com o chatbot. Você pode testar a API enviando uma pergunta e obtendo a resposta gerada pelo modelo.

---

## Como funciona o código:

- O **FastAPI** recebe as requisições através do endpoint `/chat/send`.
- A requisição é processada pela função `send_message`, que envia a pergunta para o modelo Hugging Face (**TeenyTinyLlama-460m**).
- O modelo gera a resposta, que é retornada ao usuário.

O modelo é carregado dinamicamente a partir do Hugging Face com a biblioteca `transformers`, sem a necessidade de baixar arquivos `.bin` manualmente.

---

## Observações:

- O projeto usa **Torch** para utilizar o modelo, então é recomendado ter uma GPU para um melhor desempenho.
- **CORS** foi configurado para permitir requisições de qualquer origem.

Se tiver qualquer dúvida ou quiser adicionar mais funcionalidades, entre em contato!