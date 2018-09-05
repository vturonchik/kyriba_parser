import csv
from datetime import datetime
from base_parser import BaseParser


class CSVParser(BaseParser):

    def cl_desc(self):
        return 'csv'

    def help_message(self):
        return 'Data from the CSV format will be output in the following format\n' \
               'Bank: {bank field}, Country: {country field}, City: {city field}, Account: {account filed}'

    def parser(self, path):
        output = []
        try:
            with open(path) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    output.append('Bank: <{}>, Country: <{}>, City: <{}>, Account: <{}>'
                                  .format(row['Bank'], row['Country'], row['City'], row['Account']))
            return output
        except Exception as err_mes:
            with open('log.txt', 'a') as log_file:
                log_file.write('{} - {}\n'.format(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(err_mes)))
                print('Error written to log file.')
