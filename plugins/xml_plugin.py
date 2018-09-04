from xml.etree import cElementTree as ET
from datetime import datetime
from base_parser import BaseParser


class XMLParser(BaseParser):

    def cl_desc(self):
        return 'xml'

    def help_message(self):
        return 'Data from the XML format will be output in the following format\n' \
               'Bank: {bank field}, Country: {country field}, City: {city field}, Account: {account filed}'

    def parser(self, path_to_file):
        output = []
        try:
            tree = ET.ElementTree(file=path_to_file)
            root = tree.getroot()
            for child in root:
                elements_list = []
                if child.tag == 'Client':
                    for step_child in child:
                        elements_list.append('{}: <{}>'.format(step_child.tag, step_child.text))
                    output.append(', '.join(elements_list))
            return output
        except Exception as err_mes:
            with open('log.txt', 'a') as log_file:
                log_file.write('{} - {}\n'.format(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(err_mes)))
                print('Error written to log file.')
