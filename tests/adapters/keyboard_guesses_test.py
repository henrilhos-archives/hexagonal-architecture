import unittest.mock

from src.adapters.keyboard_guesses import KeyboardGuesses


class MyTestCase(unittest.TestCase):
    def test_something(self):
        keyboard_guesses = KeyboardGuesses()

        with unittest.mock.patch('builtins.input', return_value='5'):
            self.assertEqual(keyboard_guesses.latest_guess(), 5)

        with unittest.mock.patch('builtins.input', return_value='10'):
            self.assertEqual(keyboard_guesses.latest_guess(), 10)


if __name__ == '__main__':
    unittest.main()
