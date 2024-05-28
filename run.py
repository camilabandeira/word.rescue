import os
import pyfiglet
from rich.console import Console
from rich.padding import Padding
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

console = Console()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_rules():
    rules = (
        "[bold yellow]1.[/bold yellow] You will be given "
        "clues about a famous person"
        "from history.\n"
        "[bold yellow]2.[/bold yellow] Based on the clues, "
        "you have to identify the"
        "person.\n"
        "[bold yellow]3.[/bold yellow] You can ask "
        "for up to [bold yellow]3[/bold yellow]"
        "additional hints for each person.\n"
        "[bold yellow]4.[/bold yellow] The game ends "
        "after [bold yellow]5[/bold yellow]"
        "rounds, and your score will be displayed.\n"
        "[bold yellow]5.[/bold yellow] Have fun and learn "
        "new facts along the way!\n"
    )
    rules_text = Text.from_markup(rules, justify="left")
    rules_panel = Panel(
        rules_text,
        title="Game Rules",
        border_style="magenta",
        expand=False,
        padding=(1, 2)
    )
    aligned_rules = Align(rules_panel, align="center")
    console.print(aligned_rules)


def main():
    clear_screen()

    BANNER = pyfiglet.figlet_format(
        "Word Rescue", justify="center", font="doom"
    )
    padded_banner = Padding(BANNER, (0, 4))
    console.print(padded_banner)

    welcome_message = (
        "The fun and educational word game that challenges you to identify "
        "famous people from history based on intriguing clues about their "
        "lives and achievements. Perfect for history lovers, students, and "
        "trivia fans, this game lets you learn while you play.\n"
    )
    aligned_message = Align(welcome_message, align="center")
    padded_message = Padding(aligned_message, (0, 2))
    console.print(padded_message)

    prompt_message = Align("Please enter your name:", align="center")
    console.print(prompt_message)

    console_width = console.size.width
    user_name = ""

    while not user_name.strip():
        user_name = console.input(
            f"{' ' * ((console_width - len('Please enter your name:')) // 2)}"
        )
        if not user_name.strip():
            error_message = Text(
                "Invalid input. Please enter your name:", style="bold red"
            )
            aligned_error = Align(error_message, align="center")
            console.print(aligned_error)

    clear_screen()

    welcome_text = f"Welcome, {user_name}!"
    aligned_welcome = Align(welcome_text, align="center", style="bold")
    padded_welcome = Padding(aligned_welcome, (2, 0))
    console.print(padded_welcome)

    rules_prompt = Align(
        "Would you like to read the rules? (yes/no):", align="center"
    )
    console.print(rules_prompt)

    wants_rules = ""
    while wants_rules.lower() not in ["yes", "no"]:
        wants_rules = console.input(
            f"{' ' * ((console_width - len('Would you like to read the rules? '
               '(yes/no):')) // 2)}"
        )
        if wants_rules.lower() not in ["yes", "no"]:
            error_message = Text(
                "Invalid input. Please enter 'yes' or 'no':", style="bold red"
            )
            aligned_error = Align(error_message, align="center")
            console.print(aligned_error)

    if wants_rules.lower() == "yes":
        clear_screen()
        display_rules()

    level_prompt = Align(
        "Please select the game level (easy, medium, hard):", align="center"
    )
    console.print(level_prompt)

    game_level = ""
    while game_level.lower() not in ["easy", "medium", "hard"]:
        game_level = console.input(
            f"{' ' * ((console_width - len('Please select the game level '
               '(easy, medium, hard):')) // 2)}"
        )
        if game_level.lower() not in ["easy", "medium", "hard"]:
            error_message = Text(
                "Invalid input. Please enter 'easy', 'medium', or 'hard':",
                style="bold red"
            )
            aligned_error = Align(error_message, align="center")
            console.print(aligned_error)

    clear_screen()


if __name__ == "__main__":
    main()
