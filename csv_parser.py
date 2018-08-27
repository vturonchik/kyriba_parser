import csv
from datetime import datetime


class CsvParser:

    def __init__(self, path_to_file):
        self.path = path_to_file

    @staticmethod
    def help_message():
        print('Data from the CSV format will be output in the following format')
        print('Bank: {bank field}, Country: {country field}, City: {city field}, Account: {account filed}')

    def parser(self):
        try:
            with open(self.path) as self.csv_file:
                self.reader = csv.DictReader(self.csv_file)
                for self.row in self.reader:
                    print('Bank: {%s}, Country: {%s}, City: {%s}, Account: {%s}' %
                          (self.row['Bank'], self.row['Country'], self.row['City'], self.row['Account']))
        except IOError as e:
            with open('log.txt', 'a+') as log_file:
                log_file.write('%s - %s\n' % (datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(e)))
