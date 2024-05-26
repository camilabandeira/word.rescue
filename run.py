import os
import pyfiglet
from rich.console import Console
from rich.padding import Padding
from rich.align import Align
from rich.text import Text

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    BANNER = pyfiglet.figlet_format("Word Rescue", justify="center", font="doom")
    padded_banner = Padding(BANNER, (0, 4))  # Reduced vertical padding to 0
    console.print(padded_banner)

    welcome_message = (
        "The fun and educational word game that challenges you to identify "
        "famous people from history based on intriguing "
        "clues about their lives "
        "and achievements. Perfect for history lovers, "
        "students, and trivia fans, "
        "this game lets you learn while you play." + "\n"
    )
    aligned_message = Align(welcome_message, align="center")
    padded_message = Padding(aligned_message, (0, 2))  # Reduced vertical padding to 0
    console.print(padded_message)

    prompt_message = Align("Please enter your name:", align="center")
    console.print(prompt_message)

    console_width = console.size.width
    user_name = ""

    while not user_name.strip():
        user_name = console.input(f"{' ' * ((console_width - len('Please enter your name:')) // 2)}")
        if not user_name.strip():
            error_message = Text("Invalid input. Please enter your name:", style="bold red")
            aligned_error = Align(error_message, align="center")
            console.print(aligned_error)

    clear_screen()

    welcome_text = f"Welcome, {user_name}!"
    aligned_welcome = Align(welcome_text, align="center", style="bold")
    padded_welcome = Padding(aligned_welcome, (2, 0))  # Add padding around the welcome message
    console.print(padded_welcome)

if __name__ == "__main__":
    main()
