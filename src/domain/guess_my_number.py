from src.domain.display import Display
from src.domain.guesses import Guesses


class GuessMyNumber:
    def __init__(self, number_to_guess: int, guesses: Guesses, display: Display):
        self.number_to_guess = number_to_guess
        self.guesses = guesses
        self.display = display

    def play(self):
        self.display_introduction()
        guessed_correctly = self.give_player_up_to_five_attempts_to_guess()

        self.display_final_result(guessed_correctly)

    def give_player_up_to_five_attempts_to_guess(self) -> bool:
        attempt_number = 1
        guessed_correctly = False

        while attempt_number <= 5 and not guessed_correctly:
            self.display_prompt(attempt_number)

            if self.guesses.latest_guess() == self.number_to_guess:
                guessed_correctly = True
            else:
                self.display.show("Tente novamente")

            attempt_number += 1

        return guessed_correctly

    def display_prompt(self, attempt_number: int):
        self.display.show(f"Seu palpite? (tentativa {attempt_number})")

    def display_introduction(self):
        self.display.show("Estou pensando em um número entre 1 e 10...")
        self.display.show("Será que você consegue acertar em 5 tentativas?")

    def display_final_result(self, guessed_correctly: bool):
        if guessed_correctly:
            self.display.show("Parabéns! Você acertou!")
        else:
            self.display.show("Infelizmente você errou todas as tentativas.")
