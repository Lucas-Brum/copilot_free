import threading
import requests
import os

def preload_model(ollama_url, model_name):
    data = {
        "model": model_name,
        "prompt": "", 
        "stream": False
    }
    try:
        requests.post(ollama_url, json=data)
    except:
        pass  

def send_prompt(prompt, model_name, ollama_url):
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(ollama_url, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "Response not found.")
    
    except requests.exceptions.RequestException as e:
        return f"Error calling Ollama API: {e}"

def read_settings(filepath):
    try:
        with open(os.path.abspath(filepath), 'r', encoding='utf-8') as file:
            settings = {}
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    settings[key.strip()] = value.strip()
            return settings
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    settings = read_settings("./settings.txt")
    if not settings:
        print("Settings file not found or empty.")
        print("Read about in readme.txt -> Configuration")
        return

    ollama_url = settings.get("OLLAMA_URL")
    model_name = settings.get("MODEL_NAME")

    continue_responding = True

    threading.Thread(target=preload_model, args=(ollama_url, model_name), daemon=True).start()
    
    while continue_responding:
        prompt = input("Type something: ")
        response = send_prompt(prompt, model_name, ollama_url)

        print("AI Response:")
        print(response)

        if response.lower() == "/exit":
            continue_responding = False
            print("Exiting...")
if __name__ == "__main__":
    main()