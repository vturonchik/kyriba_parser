import argparse
import plugins_load


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
    return """Parsing for the following formats: {formats}
        --help ---------------------------------- show available formats parsers
        --format {formats} --help ---------------- show data structure
        --format {formats} --path path\\to\\file --- show data (The path to the file must not contain spaces.)"""\
        .format(formats=', '.join(available_parsers))


def actions(available_parsers):
    """
    Processing of user input.
    """

    args = cli_args(available_parsers)
    if args.help and args.format is None and args.path is None:
        print(show_help_message(available_parsers))
    elif args.format and args.help:
        if args.format not in available_parsers:
            print('Parser not found')
        for parser in plugins_load.get_parsers_instances():
            if args.format == parser.cl_desc():
                print(parser.help_message())
    elif args.format and args.path and args.help is False:
        for parser in plugins_load.get_parsers_instances():
            if args.format == parser.cl_desc():
                for row in parser.parser(args.path):
                    print(row)
    else:
        print('The specified actions were not found. Use help.')


def main():
    """
    The main entry point of the application.
    """
    parsers = plugins_load.get_available_parsers()
    actions(parsers)


if __name__ == '__main__':
    main()
