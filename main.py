import sys
from api_handler import NvidiaAPI
from chat_interface import ChatInterface
from models import get_model_selection

def main():
    model_info = get_model_selection()
    if not model_info:
        print("Invalid selection. Exiting.")
        sys.exit(1)

    api_key = model_info["api_key"]
    model = model_info["model"]
    temperature = model_info["temperature"]
    top_p = model_info["top_p"]
    max_tokens = model_info["max_tokens"]

    if not api_key:
        print("Error: API key is not set for the selected model.")
        sys.exit(1)

    nvidia_api = NvidiaAPI(api_key, model, temperature, top_p, max_tokens)
    chat_interface = ChatInterface()

    chat_interface.display_message(f"Welcome to the NVIDIA Chat Interface using {model_info['name']}!", "System")

    while True:
        try:
            user_input = chat_interface.get_user_input()
            if user_input.lower() in ["exit", "quit"]:
                chat_interface.display_message("Goodbye!", "System")
                break
            response = nvidia_api.send_request(user_input)
            chat_interface.display_message(response, "NVIDIA API")
        except KeyboardInterrupt:
            chat_interface.display_message("Interrupted. Exiting...", "System")
            break
        except Exception as e:
            chat_interface.display_message(f"Error: {str(e)}", "System")

if __name__ == "__main__":
    main()



