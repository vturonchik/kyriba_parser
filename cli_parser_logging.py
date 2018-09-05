import logging
import os


def log_write(err):
    file_path = os.path.dirname(__file__)
    logs_dir = os.path.join(file_path, 'logs')
    logging.basicConfig(
        filename=os.path.join(logs_dir, 'log.txt'),
        level=logging.WARNING,
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S',

    )
    logging.exception(err)
    print('The error is logged.')
    exit(1)
