import os
import pyfiglet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    BANNER = pyfiglet.figlet_format("Word Rescue", justify="center", font="doom")
    print(BANNER)

if __name__ == "__main__":
    main()
