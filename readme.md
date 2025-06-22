# AI Battle

Script Python para simular batalhas entre personagens utilizando a API Gemini AI do Google. 
Os personagens alternam ataques e defesas, com respostas geradas automaticamente pela IA.

## Requisitos

- Python 3.8+
- [Gemini - Generative AI Python](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br)
- Arquivo `client.py` com a variável `API_KEY` definida.

## Instalação

```bash
pip install -q -U google-genai
```

Editar arquivo `client.py`:

```python
from google import genai

AI = genai.Client(
    api_key="YOUR_API_KEY"
)
```

## Funções Principais

- `generate_battle(characters)`: Inicia uma nova batalha gerada por IA.
- `utils.dynamic_read(conversation)`: Imprime a conversa com efeito dinâmico.
- `utils.save_as_json(conversation)`: Salva a história no formato Json.
- `utils.save_as_markdown(conversation)`: Salva a história no formato Markdown.

## Exemplo de Uso

```python
# Pode ser subtituido por 2 input()
names = ["Personagem 1", "Personagem 2"]

# Gera a nova lista de conversas.
conversation = generate_battle(
    characters = names,
    turns = 10,
    word_limits = 120,
    languages = "PT-BR"
)

# Salva o arquivo
utils.save_as_json(conversation)

# Diálogo dinâmico no terminal
input("Enter para continuar...")
utils.dynamic_read(conversation)
```
