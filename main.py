from google import genai
import config, time, json

Client_AI = genai.Client(api_key= config.API_KEY)

def new_battle(characters: list, turns:int=4, words_limit:int=100, language:str="EN-US"):
    """Starts a new battle between two characters, alternating attack and defense turns.
    Args:
        characters (list): List of character names
        turns (int, optional): Number of battle turns. Default is 2.
        words_limit (int, optional): Word limit per response. Default is 100.
        language (str, optional): Response language. Default is "EN-US".
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
            "content": "You are in a battle. In each turn, describe and return only your attack or defense move, without extra explanations."
        }
    ]
    for i in range(turns):
        print(f"Requesting turn {i+1}")
        current_char = chars[i % 2]
        prompt = {
            "agent_rules": [f"You can only use {words_limit} words.", f"answer in {language} language."],
            "all_conversation": conversation,
            "last_content": conversation[-1],
            "role":"system",
            "content": f"{current_char}, it's your turn to attack! Describe your move."
        }
        move = request_completion(prompt)
        conversation.append({"role": current_char, "content": move})
    return conversation

def request_completion(prompt):
    """
    Generates a response for a prompt using the Gemini AI model.
    Args:
        prompt (str): The input prompt to be sent to the AI model for content generation.
    Returns:
        response.text: The generated content returned by the AI model.
    **Note**: This function introduces a 5-second delay before making the request.
    """
    time.sleep(5)
    response = Client_AI.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=str(prompt)
    )
    return response.text

def dinamic_print(conversation: list):
    """Prints each message in a conversation with a dynamic, character-by-character effect.
    Args:
        conversation (list): A list of dictionaries, where each dictionary 
            represents a message with at least the keys "role" (str) and "content" (str).
    """
    for message in conversation:
        print(f"{message['role']}: ")
        for char in message["content"]:
            print(char, end='', flush=True)
            time.sleep(0.06)
        print("\n")
        time.sleep(0.5)


def save_file(names: list, conversation: list):
    filename = f"{names[0]}_vs_{names[1]}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(conversation[1:], f, ensure_ascii=False, indent=2)
    print(f"\n\nFile saved as {filename}")

def main():
    person1 = input("First character name: ")
    person2 = input("Second character name: ")

    names = [person1, person2]
    conversation = new_battle(characters=names,turns=2, language="PT-BR")
    #dinamic_print(conversation)  # Optional
    save_file(names, conversation)

if __name__ == "__main__":
    main()