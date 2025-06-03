# Interface para o modelo LLaMA local via llama-cpp-python

from llama_cpp import Llama

class LlamaModelHandler:
    def __init__(self, model_path: str):
        # Inicializa o modelo local passando o caminho do arquivo .bin
        self.model = Llama(model_path=model_path)
    
    def ask(self, question: str) -> str:
        # Executa a geração de texto para a pergunta recebida
        output = self.model(prompt=question, max_tokens=150)
        # Retorna somente o texto gerado, sem espaços extras
        return output['choices'][0]['text'].strip()
