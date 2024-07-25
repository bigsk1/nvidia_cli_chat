from dotenv import load_dotenv
import os
from rich.console import Console
from rich.text import Text

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

models = {
    "1": {
        "name": "Mistral Large",
        "description": "Excels in complex multilingual reasoning tasks, including text understanding, and code generation",
        "model": os.getenv("MISTRAL_LARGE"),
        "api_key": api_key,
        "temperature": 0.5,
        "top_p": 1.0,
        "max_tokens": 1024
    },
    "2": {
        "name": "LLaMA 3 70B",
        "description": "Complex conversations with superior contextual understanding, reasoning and text generation.",
        "model": os.getenv("LLAMA3_70B"),
        "api_key": api_key,
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 1024
    },
    "3": {
        "name": "PHI 3 Mini 128K",
        "description": "Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.",
        "model": os.getenv("PHI_3_MINI_128K"),
        "api_key": api_key,
        "temperature": 0.2,
        "top_p": 0.7,
        "max_tokens": 1024
    },
    "4": {
        "name": "Arctic",
        "description": "A robust model for general-purpose AI tasks with a focus on cold data processing.",
        "model": os.getenv("ARCTIC"),
        "api_key": api_key,
        "temperature": 0.5,
        "top_p": 1.0,
        "max_tokens": 1024
    },
    "5": {
        "name": "Granite 34B Code",
        "description": "Software programming LLM for code generation, completion, explanation, and multiturn conversation.",
        "model": os.getenv("GRANITE_34B_CODE"),
        "api_key": api_key,
        "temperature": 0.5,
        "top_p": 1.0,
        "max_tokens": 1024
    },
    "6": {
        "name": "LLaMA 3 405B",
        "description": "Complex conversations with superior contextual understanding, reasoning and text generation.",
        "model": os.getenv("LLAMA3_405B"),
        "api_key": api_key,
        "temperature": 0.2,
        "top_p": 0.7,
        "max_tokens": 1024
    }
}

def get_model_selection():
    console = Console()
    for key, value in models.items():
        text = Text()
        text.append(f"{key}: ", style="bold")
        text.append(f"{value['name']}", style="bold")
        text.append(f" - {value['description']}")
        console.print(text)
        console.print("\n")
    selection = input("Select a model by number: ")
    return models.get(selection)
