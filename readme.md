# AI Battle

Script Python para simular batalhas entre personagens utilizando a API Gemini AI do Google. Os personagens alternam ataques e defesas, com respostas geradas automaticamente pela IA.

## Requisitos

- Python 3.8+
- [Gemini - Generative AI Python](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br)
- Arquivo `config.py` com a variável `API_KEY` definida.

## Instalação

```bash
pip install -q -U google-genai
```

Arquivo `config.py`:

```python
API_KEY = "SUA_CHAVE_API"
```

## Funções Principais

- `new_battle(characters)`: Inicia uma nova batalha.
- `dinamic_print(conversation)`: Imprime a conversa com efeito dinâmico.

## Exemplo de Uso

```python
person1 = input("First character name: ")
person2 = input("Second character name: ")
names = [person1, person2]
conversation = new_battle(characters=names, language="PT-BR")
save_file(names, conversation)
```
