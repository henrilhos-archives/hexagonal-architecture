import random

from src.adapters.console_display import ConsoleDisplay
from src.adapters.keyboard_guesses import KeyboardGuesses
from src.domain.display import Display
from src.domain.guess_my_number import GuessMyNumber
from src.domain.guesses import Guesses


def get_number():
    return random.randint(1, 10)


def game():
    display: Display = ConsoleDisplay()
    guesses: Guesses = KeyboardGuesses()

    GuessMyNumber(get_number(), guesses, display).play()


if __name__ == '__main__':
    game()
