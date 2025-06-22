import client, utils

def generate_battle(characters:list, turns:int=4, words_limit:int=100, language:str="PT-BR", rules:list = []):
    """Starts a new battle between two characters, alternating attack and defense turns.
    Args:
        characters (list): List of character names
        turns (int, optional): Number of battle turns. Default is 4.
        words_limit (int, optional): Word limit per response. Default is 100.
        language (str, optional): Response language. Default is "PT-BR".
        rules (list, optional): Sets new rules for the battle characters.
    Returns:
        list: List of dictionaries representing the battle conversation.
    Raises:
        ValueError: If characters list doesn't match 2 elements.
    """
    char1 = characters[0]; char2 = characters[1];
    if len(characters) != 2: raise ValueError("Characters list must contain 2 string names.");

    print("Starting a new battle. \nSetup: ")
    print(f"Character 1: {char1} | Character 2: {char2}")
    print(f"- Turns: {turns}\n- Limit: {words_limit} words\n- Language: {language}\n\n")
    chars = [char1, char2]
    conversation = [
        {
            "role": "system",
            "content": "You are in a battle. In each turn, describe and return your attack or defense move."
        }
    ]
    for i in range(turns):
        print(f"Requesting turn {i+1}")
        current_char = chars[i % 2]
        prompt = {
            "agent_rules": [
                f"You can only use {words_limit} words.", 
                f"Answer in {language} language.",
                "You need to imitate your character's speaking style.",
                rules
            ],
            "all_conversation": conversation,
            "last_content": conversation[-1],
            "role":"system",
            "content": f"{current_char}, now it's your turn to attack!"
        }
        response = client.request_completion(prompt)
        conversation.append({"role": current_char, "content": response})
    return conversation[1:]

def main():
    names = []
    rules = []
    names[0] = input("Digite o nome do primeiro personagem: ")
    names[1] = input("Digite o nome do segundo personagem: ")

    response = generate_battle(names)
    utils.dynamic_read(response)

if __name__ == "__main__":
    main()
    pass