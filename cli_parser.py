import argparse


def cli_args(available_parsers):
    """
    Creating Command-Line Arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--format',
        dest='format',
        action='store',
        choices=available_parsers,
        help='Choose available parser from: %s.' % ', '.join(available_parsers),
        required=True,
    )
    parser.add_argument(
        '--path',
        dest='path',
        action='store',
        help='Specify the absolute path to the file for parsing',
        required=False,
    )
    return parser.parse_args()


if __name__ == '__main__':

    AVAILABLE_PARSERS = ['xml', 'csv']

    cli_args(AVAILABLE_PARSERS)
