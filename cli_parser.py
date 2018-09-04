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
    print('Parsing for the following formats: {}'.format(', '.join(available_parsers)))


def actions(available_parsers):
    """
    Processing of user input.
    """

    args = cli_args(available_parsers)
    packages, plugins = plugins_load.get_plugins()
    if args.help and args.format is None and args.path is None:
        show_help_message(available_parsers)
    elif args.format and args.help:
        for plugin in plugins:
            module_obj = getattr(packages, plugin)
            if args.format == module_obj.cl_desc():
                module_obj.help_message()
    elif args.format and args.path and args.help is False:
        for plugin in plugins:
            module_obj = getattr(packages, plugin)
            if args.format == module_obj.cl_desc():
                module_obj.parser(args.path)
    else:
        print('The specified actions were not found. Use help.')


def main():
    parsers = plugins_load.get_available_parsers()
    actions(parsers)


if __name__ == '__main__':
    main()
