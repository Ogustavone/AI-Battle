import json, time, os

# Saving functions
def save_as_json(names, conversation: list):
    filename = f"./logs/{names[0]}_vs_{names[1]}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(conversation, file, ensure_ascii=False, indent=4)
    print(f"Json file saved in {os.path.abspath(filename)}")

def save_as_markdown(names, conversation: list):
    filename = f"./logs/{names[0]}_vs_{names[1]}.md"
    with open(filename, "a", encoding="utf-8") as md_file:
        for item in conversation:
            md_file.write(f"> **{item["role"]}:**\n> {item["content"]}\n")
    print(f"Markdown file saved in {os.path.abspath(filename)}")

# Read json file
def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        conversation = json.load(file)
    return conversation

def dynamic_read(conversation: list):
    """Prints each message in a conversation with a dynamic, character-by-character effect.
    Args:
        conversation (list): A list of dictionaries, where each dictionary 
            represents a message with at least the keys "role" (str) and "content" (str).
    """
    clear_terminal()
    for message in conversation:
        print(f"{message['role']}: ")
        for char in message["content"]:
            print(char, end='', flush=True)
            time.sleep(0.06)
        print()
        time.sleep(0.5)

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
