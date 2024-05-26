import os
import pyfiglet
from rich.console import Console
from rich.padding import Padding
from rich.prompt import Prompt
from rich.align import Align
from rich.text import Text

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    BANNER = pyfiglet.figlet_format("Word Rescue", justify="center", font="doom")
    padded_banner = Padding(BANNER, (1, 4))
    console.print(padded_banner)

    welcome_message = (
        "The fun and educational word game that challenges you to identify "
        "famous people from history based on intriguing clues about their lives and achievements. "
        "Perfect for history lovers, students, and trivia fans, this game lets you learn while you play."
    )
    aligned_message = Align(welcome_message, align="center", style="#DAC3F8")
    padded_message = Padding(aligned_message, (1, 2))
    console.print(padded_message)

    prompt_message = Align("Please enter your name:", align="center")
    console.print(prompt_message)

    console_width = console.size.width
    user_name = console.input(f"{' ' * ((console_width - len('Please enter your name:')) // 2)}")

    clear_screen()

    console.print(f"Welcome, {user_name}!", justify="center", style="bold")

if __name__ == "__main__":
    main()
