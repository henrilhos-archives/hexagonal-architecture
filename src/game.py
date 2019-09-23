from src.adapters.console_display import ConsoleDisplay
from src.adapters.keyboard_guesses import KeyboardGuesses
from src.domain.display import Display
from src.domain.guess_my_number import GuessMyNumber
from src.domain.guesses import Guesses


def game():
    display: Display = ConsoleDisplay()
    guesses: Guesses = KeyboardGuesses()

    GuessMyNumber(3, guesses, display).play()


if __name__ == '__main__':
    game()
