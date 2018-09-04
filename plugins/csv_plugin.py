import csv
from datetime import datetime


def cl_desc():
    return 'csv'


def help_message():
    print('Data from the CSV format will be output in the following format')
    print('Bank: {bank field}, Country: {country field}, City: {city field}, Account: {account filed}')


def parser(path_to_file):
    try:
        with open(path_to_file) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print('Bank: <{}>, Country: <{}>, City: <{}>, Account: <{}>'
                      .format(row['Bank'], row['Country'], row['City'], row['Account']))
    except Exception as err_mes:
        with open('log.txt', 'a') as log_file:
            log_file.write('{} - {}\n'.format(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(err_mes)))
            print('Error written to log file.')
