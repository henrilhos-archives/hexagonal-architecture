import io
import unittest.mock

from src.adapters.console_display import ConsoleDisplay


class ConsoleDisplayTest(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show(self, mock_stdout):
        console_display: ConsoleDisplay = ConsoleDisplay()
        console_display.show('foo')

        self.assertEqual(mock_stdout.getvalue(), 'foo\n')


if __name__ == '__main__':
    unittest.main()
