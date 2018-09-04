from xml.etree import cElementTree as ET
from datetime import datetime


def cl_desc():
    return 'xml'


def help_message():
    print('Data from the XML format will be output in the following format')
    print('Bank: {bank field}, Country: {country field}, City: {city field}, Account: {account filed}')


def parser(path_to_file):
    try:
        tree = ET.ElementTree(file=path_to_file)
        root = tree.getroot()

        for child in root:
            elements_list = []
            if child.tag == 'Client':
                for step_child in child:
                    elements_list.append('{}: <{}>'.format(step_child.tag, step_child.text))
                print(', '.join(elements_list))
    except Exception as err_mes:
        with open('log.txt', 'a') as log_file:
            log_file.write('{} - {}\n'.format(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(err_mes)))
            print('Error written to log file.')
