from xml.etree import cElementTree as ET
from datetime import datetime


class XmlParser:

    def __init__(self, path_to_file):
        self.path = path_to_file

    @staticmethod
    def help_message():
        print('Data from the XML format will be output in the following format')
        print('Bank: {bank field}, Country: {country field}, City: {city field}, Account: {account filed}')

    def parser(self):
        try:
            self.tree = ET.ElementTree(file=self.path)
            self.root = self.tree.getroot()

            for self.child in self.root:
                self.elements_list = []
                if self.child.tag == 'Client':
                    for self.step_child in self.child:
                        self.elements_list.append('%s: {%s}' % (self.step_child.tag, self.step_child.text))
                    print(', '.join(self.elements_list))
        except IOError as e:
            with open('log.txt', 'a+') as log_file:
                log_file.write('%s - %s\n' % (datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(e)))
