import unittest
from plugins.xml_plugin import XMLParser
from plugins.csv_plugin import CSVParser
import plugins_load as pl


class PluginsLoadTests(unittest.TestCase):
    def test_get_plugins(self):
        """
        Check the return of the correct list.
        """
        self.assertListEqual(pl.get_plugins()[1], ['csv_plugin', 'xml_plugin'])

    def test_get_parsers_instances(self):
        """
        Checking instances.
        """
        self.assertIsInstance(pl.get_parsers_instances()[0], CSVParser)

    def test_get_path_to_plugins(self):
        """
        Check the correct paths to the plugins.
        """
        self.assertListEqual(pl.get_path_to_plugins('settings.conf'), ['plugins', 'C:\\plug1'])


class XMLParserTest(unittest.TestCase):
    def test_xml_parser(self):
        """
        Check the correct operation of the XML parser.
        """
        xml_parser = XMLParser()
        self.assertIn('Bank: <RZB>, Country: <Switzerland>, City: <Zurich>, Account: <235425425>',
                      xml_parser.parser('c:\\xml_file.xml'))


class CSVParserTest(unittest.TestCase):
    def test_csv_parser(self):
        """
        Check the correct operation of the CSV parser.
        """
        csv_parser = CSVParser()
        self.assertIn('Bank: <RZB>, Country: <Belgium>, City: <Brussele>, Account: <1426224325>',
                      csv_parser.parser('c:\\csv_file.csv'))


if __name__ == '__main__':
    unittest.main()
