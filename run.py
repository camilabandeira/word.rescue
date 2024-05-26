import os
import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.padding import Padding

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()  # Clear the screen

    BANNER = pyfiglet.figlet_format("Word Rescue", justify="center", font="doom")
    padded_banner = Padding(BANNER, (1, 4))  # Add margin around the banner
    console.print(padded_banner)  # Print the banner with padding

    table = Table()  # Create a table with a welcome message
    table.add_column("Welcome to Word Rescue", justify="center", style="magenta")  # Add columns to the table

    table.add_row("The fun and educational word game that challenges you to identify "
                  "famous people from history based on intriguing clues about their lives and achievements. "
                  "Perfect for history lovers, students, and trivia fans, this game lets you learn while you play.")  # Add rows to the table

    padded_table = Padding(table, (1, 2))  # Add margin around the table
    console.print(padded_table)  # Print the table with padding

if __name__ == "__main__":
    main()
