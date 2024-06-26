import os
import pyfiglet
from rich.console import Console
from rich.padding import Padding
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
import random

# Initialize the console for rich text display
console = Console()


# Function to clear the screen based on the OS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display the game rules using rich text formatting
def display_rules():
    rules = (
        "[bold yellow]1.[/bold yellow] You will be given "
        "clues about a famous person from history.\n"
        "[bold yellow]2.[/bold yellow] Based on the clues, "
        "you have to identify the person.\n"
        "[bold yellow]3.[/bold yellow] You can ask "
        "for up to [bold yellow]3[/bold yellow] "
        "additional hints for each person.\n"
        "[bold yellow]4.[/bold yellow] The game ends "
        "after [bold yellow]5[/bold yellow] rounds, and your "
        "score will be displayed.\n"
        "[bold yellow]5.[/bold yellow] Have fun and "
        "learn new facts along the way!\n"
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


# Dictionary to hold historical figures categorized by difficulty level
historical_figures = {
    "easy": [
        {"name": "Cleopatra", "clues": [
            "Queen of Egypt",
            "Had relationships with Julius Caesar and Mark Antony",
            "Known for her beauty and intelligence"
        ]},
        {"name": "Napoleon", "clues": [
            "French military leader",
            "Emperor of the French",
            "Exiled to the island of Elba"
        ]},
        {"name": "Joan of Arc", "clues": [
            "French heroine",
            "Led the French army to victory",
            "Burned at the stake"
        ]},
        {"name": "Leonardo da Vinci", "clues": [
            "Italian polymath",
            "Painted the Mona Lisa",
            "Designed early flying machines"
        ]}
    ],
    "medium": [
        {"name": "Plato", "clues": [
            "Classical Greek philosopher",
            "Student of Socrates",
            "Teacher of Aristotle"
        ]},
        {"name": "Shakespeare", "clues": [
            "English playwright and poet",
            "Wrote 'Hamlet' and 'Romeo and Juliet'",
            "Born in Stratford-upon-Avon"
        ]},
        {"name": "Marie Curie", "clues": [
            "Pioneering physicist and chemist",
            "First woman to win a Nobel Prize",
            "Discovered radium and polonium"
        ]},
        {"name": "Genghis Khan", "clues": [
            "Founder of the Mongol Empire",
            "United the Mongol tribes",
            "Conquered large parts of Asia"
        ]}
    ],
    "hard": [
        {"name": "Aristotle", "clues": [
            "Classical Greek philosopher",
            "Student of Plato",
            "Tutor of Alexander the Great"
        ]},
        {"name": "Homer", "clues": [
            "Ancient Greek poet",
            "Author of 'The Iliad' and 'The Odyssey'",
            "Known for epic poetry"
        ]},
        {"name": "Nicolaus Copernicus", "clues": [
            "Renaissance mathematician and astronomer",
            "Formulated a model of the universe",
            "Placed the Sun at the center of the universe"
        ]},
        {"name": "Immanuel Kant", "clues": [
            "German philosopher",
            "Wrote 'Critique of Pure Reason'",
            "Major figure in modern philosophy"
        ]}
    ]
}


# Function to reset the used figures for a new game
def reset_used_figures():
    global used_figures
    used_figures = {
        "easy": [],
        "medium": [],
        "hard": []
    }


# Get a random historical figure from the specified difficulty level
def get_random_figure(level):
    available_figures = [
        fig for fig in historical_figures[level]
        if fig not in used_figures[level]
    ]
    if not available_figures:
        return None
    figure = random.choice(available_figures)
    used_figures[level].append(figure)
    return figure


# Function to display the current progress of the guessed word
def display_word_progress(word, guessed_letters):
    display = "".join([
        letter if letter.lower() in guessed_letters else "_"
        for letter in word
    ])
    return f"Word: {display}"


# Function to display the letters that have already been guessed
def display_guessed_letters(guessed_letters):
    guessed_display = ", ".join(sorted(guessed_letters)).upper()
    return f"[bold red]{guessed_display}[/bold red]"


# Function to play a single round of the game
def play_round(level, round_number):
    figure = get_random_figure(level)
    if figure is None:
        console.print(
            Align("No more unique figures available for this level.",
                  align="center", style="bold red"))
        return 0
    attempts = {"easy": 6, "medium": 4, "hard": 3}[level]
    guessed_letters = set()

    while attempts > 0:
        word_progress = display_word_progress(figure['name'], guessed_letters)
        guessed_display = display_guessed_letters(guessed_letters)

        panel_content = (
            f"[yellow]Clue:[/yellow] {figure['clues'][0]}\n\n"
            f"{word_progress}\n\n"
            f"Guessed letters: {guessed_display}\n\n"
            f"Attempts remaining: [green]{attempts}[/green]"
        )
        panel = Panel(panel_content, title=f"Round {round_number}",
                      border_style="magenta", padding=(1, 2))
        aligned_panel = Align(panel, align="center")
        console.print(aligned_panel)

        guess_prompt = "Guess a letter: "
        console_width = console.size.width
        padding = ' ' * ((console_width - len(guess_prompt)) // 2)
        guess = console.input(f"{padding}{guess_prompt}").strip().lower()

        clear_screen()

        if not guess.isalpha() or len(guess) != 1:
            console.print(
                Align("Invalid input. Please guess a single letter.",
                      align="center", style="bold red"))
        elif guess in guessed_letters:
            console.print(
                Align("You already guessed that letter.",
                      align="center", style="bold red"))
        else:
            guessed_letters.add(guess)
            if guess in figure['name'].lower():
                console.print(
                    Align("Correct guess!", align="center",
                          style="bold green"))
            else:
                attempts -= 1
                console.print(
                    Align(
                        f"Incorrect guess.",
                        align="center", style="bold red"))

        if all(letter.lower() in guessed_letters
               for letter in figure['name'] if letter != " "):
            console.print(
                Align(f"Correct! The answer is {figure['name']}.",
                      align="center", style="bold green"))
            return 1

    clear_screen()
    final_panel_content = (
        f"The answer was [bold green]{figure['name']}[/bold green].\n"
    )
    final_panel = Panel(
        Align(final_panel_content, align="center"), title="Round Over",
        border_style="magenta", padding=(1, 0)
    )
    padded_final_panel = Padding(final_panel, (1, 10))
    console.print(Align(padded_final_panel, align="center"))

    return 0


# Main function to start the game
def main():
    clear_screen()

    # Display game banner
    BANNER = pyfiglet.figlet_format("Word Rescue", font="doom")
    padded_banner = Padding(BANNER, (0, 4))
    aligned_banner = Align(padded_banner, align="center")
    console.print(aligned_banner)

    # Display welcome message
    welcome_message = (
        "The fun and educational word game that challenges you to identify "
        "famous people from history based on intriguing clues about their "
        "lives and achievements. Perfect for history lovers, students, and "
        "trivia fans, this game lets you learn while you play.\n"
    )
    aligned_message = Align(welcome_message, align="center")
    padded_message = Padding(aligned_message, (0, 2))
    console.print(padded_message)

    # Prompt user to enter their name
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

    # Welcome user by name
    welcome_text = f"Welcome, [yellow]{user_name}[/yellow]!"
    aligned_welcome = Align(welcome_text, align="center", style="bold")
    padded_welcome = Padding(aligned_welcome, (2, 0))
    console.print(padded_welcome)

    # Prompt user to see if they want to read the rules
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
                "Invalid input. Please enter 'yes' or 'no':",
                style="bold red"
            )
            aligned_error = Align(error_message, align="center")
            console.print(aligned_error)

    clear_screen()

    if wants_rules.lower() == "yes":
        display_rules()

    # Prompt user to select game level
    level_prompt = Align(
        "Please select the game level ([bold]easy[/bold], [bold]medium[/bold],"
        "[bold]hard[/bold]):", align="center"
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
    # Rounds of the game
    rounds = 4
    score = 0
    # Reset Figures
    reset_used_figures()

    for round_number in range(1, rounds + 1):
        score += play_round(game_level, round_number)
        if round_number < rounds:
            next_round_prompt = Align(
                "[bold italic]Press enter to the next round.[/bold italic]",
                align="center"
            )
            console.print(next_round_prompt)
            console.input()

        clear_screen()

    final_score_text = (
        f"Your final score is [yellow]{score}[/yellow] out, "
        f"of [yellow]{rounds}[/yellow]."
    )
    aligned_final_score = Align(final_score_text, align="center", style="bold")
    console.print(aligned_final_score)

    # Prompt user to see if they want to play again
    replay_prompt = Align(
        "Would you like to play again? (yes/no):", align="center"
    )
    console.print(replay_prompt)

    play_again = ""
    while play_again.lower() not in ["yes", "no"]:
        play_again = console.input(
            f"{' ' * ((console_width - len('Would you like to play again? '
               '(yes/no):')) // 2)}"
        )
        if play_again.lower() not in ["yes", "no"]:
            error_message = Text(
                "Invalid input. Please enter 'yes' or 'no':",
                style="bold red"
            )
            aligned_error = Align(error_message, align="center")
            console.print(aligned_error)

    if play_again.lower() == "yes":
        clear_screen()
        main()
    else:
        clear_screen()
        goodbye_message = pyfiglet.figlet_format("Goodbye!", font="doom")
        padded_goodbye = Padding(goodbye_message, (0, 4))
        aligned_goodbye = Align(padded_goodbye, align="center")
        console.print(aligned_goodbye)
        

if __name__ == "__main__":
    main()
