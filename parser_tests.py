import unittest
import cli_parser as cli


class CLIParserTests(unittest.TestCase):
    def test_get_available_parsers(self):
        """
        Check the return of the correct type.
        """
        self.assertIsInstance(cli.get_available_parsers('settings.conf'), list)


if __name__ == '__main__':
    unittest.main()
