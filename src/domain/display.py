import abc


class Display(abc.ABC):
    @abc.abstractmethod
    def show(self, text: str):
        pass
