from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown

class ChatInterface:
    def __init__(self):
        self.console = Console()

    def display_message(self, message, sender="System"):
        self.console.print(Markdown(f"**{sender}:** {message}"))
        self.console.print("\n")  

    def get_user_input(self):
        return Prompt.ask("You")
