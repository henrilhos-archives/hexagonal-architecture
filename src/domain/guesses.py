import abc


class Guesses(abc.ABC):
    @abc.abstractmethod
    def latest_guess(self) -> int:
        pass
