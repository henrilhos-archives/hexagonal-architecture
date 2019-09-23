from src.domain.guesses import Guesses


class KeyboardGuesses(Guesses):
    def latest_guess(self) -> int:
        number = input()
        return int(number)
