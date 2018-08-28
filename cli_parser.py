import argparse
import xml_plugin as xml
import csv_plugin as csv


def cli_args(available_parsers):
    """
    Creating Command-Line Arguments
    """

    parser = argparse.ArgumentParser(
        description='CLI utility for parsing any files formats',
        add_help=False,
        usage='''
        --help ---------------------------------- for show available formats parsers
        --format {formats} --help ---------------- for show data structure
        --format {formats} --path path\\to\\file --- for show data
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
    res = cli_args(available_parsers)
    if res.help and res.format is None and res.path is None:
        show_help_message(available_parsers)
    elif res.format and res.help:
        if res.format == 'csv':
            csv.help_message()
        elif res.format == 'xml':
            xml.help_message()
        else:
            print('The specified parser was not found.')
    elif res.format and res.path and res.help is False:
        if res.format == 'csv':
            csv.parser(res.path)
        elif res.format == 'xml':
            xml.parser(res.path)
    else:
        print('The specified actions were not found. Use help.')


if __name__ == '__main__':
    AVAILABLE_PARSERS = ['xml', 'csv']
    actions(AVAILABLE_PARSERS)
