from src.domain.display import Display


class ConsoleDisplay(Display):
    def show(self, text: str):
        print(text)
