import argparse
from datetime import datetime
import xml_plugin as xml
import csv_plugin as csv
try:
    import ConfigParser as configparser
except ImportError:
    import configparser


def cli_args(available_parsers):
    """
    Creating Command-Line Arguments
    """

    parser = argparse.ArgumentParser(
        description='CLI utility for parsing any files formats',
        add_help=False,
        usage='''
        --help ---------------------------------- show available formats parsers
        --format {formats} --help ---------------- show data structure
        --format {formats} --path path\\to\\file --- show data (The path to the file must not contain spaces.)
        '''.format(formats=', '.join(available_parsers))
    )
    parser.add_argument(
        '--help',
        dest='help',
        action='store_true',
        required=False,
    )
    parser.add_argument(
        '--format',
        dest='format',
        action='store',
    )
    parser.add_argument(
        '--path',
        dest='path',
        action='store',
        required=False,
    )
    return parser.parse_args()


def show_help_message(available_parsers):
    print('Parsing for the following formats {%s}' % ', '.join(available_parsers))


def actions(available_parsers):
    """
    Processing of user input.
    """

    args = cli_args(available_parsers)
    if args.help and args.format is None and args.path is None:
        show_help_message(available_parsers)
    elif args.format and args.help:
        if args.format == 'csv':
            csv.help_message()
        elif args.format == 'xml':
            xml.help_message()
        else:
            print('The specified parser was not found.')
    elif args.format and args.path and args.help is False:
        if args.format == 'csv':
            csv.parser(args.path)
        elif args.format == 'xml':
            xml.parser(args.path)
    else:
        print('The specified actions were not found. Use help.')


def get_available_parsers(path_to_conf):
    """
    Return list of parsers from config file
    """

    config = configparser.ConfigParser()
    config.read(path_to_conf)
    try:
        available_parsers = config.get('Settings', 'parsers')
        return [i.strip() for i in available_parsers.split(',')]
    except Exception as err_mes:
        with open('log.txt', 'a') as log_file:
            log_file.write('%s - %s\n' % (datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(err_mes)))
        print('%s in file %s' % (str(err_mes), path_to_conf))
        exit(0)


if __name__ == '__main__':
    parsers = get_available_parsers('settings.conf')
    actions(parsers)
