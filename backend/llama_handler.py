from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Classe responsável por carregar e interagir com o modelo de linguagem
class LlamaModelHandler:
    def __init__(self):
        # Carrega o tokenizador e o modelo diretamente do Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained("nicholasKluge/TeenyTinyLlama-460m")
        self.model = AutoModelForCausalLM.from_pretrained("nicholasKluge/TeenyTinyLlama-460m")

        # Define o dispositivo de execução (GPU ou CPU)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    # Método para gerar a resposta baseada na pergunta fornecida
    def ask(self, question: str) -> str:
        # Tokeniza a entrada e move os dados para o dispositivo (GPU ou CPU)
        inputs = self.tokenizer(question, return_tensors="pt").to(self.device)

        # Gera a resposta com o modelo
        completions = self.model.generate(**inputs, num_return_sequences=1, max_new_tokens=100)

        # Decodifica e retorna a resposta gerada
        return self.tokenizer.decode(completions[0], skip_special_tokens=True)