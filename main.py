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
        oponent = chars[(i + 1) % 2]
        prompt = {
            "agent_rules": [
                f"You can only use {words_limit} words.", 
                f"Answer in {language} language.",
                "You need to imitate your character's speaking style.",
                "Avoid redundancy; if a point was already made, confirm or expand naturally without repeating."
                "Never reuse phrases or structures from past turns. If a concept was mentioned before, rephrase it uniquely or add new tactical depth.",
                "Don't use markdown or html tags.",
                "Never use line breaks. Respond in a single paragraph."
                "User_rules have maximum precedence.",
            ],
            "user_rules": rules,
            "oponent": oponent,
            "all_conversation": conversation,
            "last_content": conversation[-1],
            "role":"system",
            "content": f"{current_char}, It's your turn. Describe your next move."
        }
        response = client.request_completion(prompt)
        conversation.append({"role": current_char, "content": response})
    return conversation[1:]

def main():
    utils.clear_terminal()
    input1 = input("Digite o nome do primeiro personagem: ")
    input2 = input("Digite o nome do segundo personagem: ")
    names = [input1, input2]

    response = generate_battle(names)
    utils.dynamic_read(response)

if __name__ == "__main__":
    main()
    pass