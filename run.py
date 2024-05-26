import os
import pyfiglet
from rich.console import Console
from rich.table import Table

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()  # Clear the screen

    BANNER = pyfiglet.figlet_format("Word Rescue", justify="center", font="doom")
    print(BANNER)  # Print the banner

    table = Table()  # Create a table with a welcome message

    table.add_column("Welcome to Word Rescue", justify="center", style="magenta")  # Add columns to the table

    table.add_row("The fun and educational word game that challenges you to identify "
                  "famous people from history based on intriguing clues about their lives and achievements. "
                  "Perfect for history lovers, students, and trivia fans, this game lets you learn while you play.")  # Add rows to the table

    console.print(table)

if __name__ == "__main__":
    main()
