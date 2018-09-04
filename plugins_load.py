import os
from datetime import datetime
try:
    import ConfigParser as configparser
except ImportError:
    import configparser
import inspect
from plugins.base_parser import BaseParser


def get_plugins():
    """
    Imports plugins in the specified paths.
    """
    paths = get_path_to_plugins('settings.conf')
    plugins = []
    package_obj = None
    for path in paths:
        files = os.listdir(path)
        for f_name in files:
            if f_name.endswith('.py'):
                module_name = f_name[:-3]
                if path[-1] == '\\':
                    module_dir = os.path.split(path[:-1])[1]
                else:
                    module_dir = os.path.split(path)[1]
                if module_name != "__init__" and module_name != 'base_parser':
                    package_obj = __import__('{}.{}'.format(module_dir, module_name))
                    plugins.append(module_name)
    return package_obj, plugins


def get_path_to_plugins(path_to_conf):
    """
    Gets the paths to the plugin folders from the configuration file.
    """
    config = configparser.ConfigParser()
    config.read(path_to_conf)
    try:
        available_parsers = config.get('Settings', 'plugins_dir')
        return [i.strip() for i in available_parsers.split(',') if i]
    except Exception as err_mes:
        with open('log.txt', 'a') as log_file:
            log_file.write('{} - {}\n'.format(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S'), str(err_mes)))
        print('{} in file {}'.format(str(err_mes), path_to_conf))
        exit(0)


def get_parsers_instances():
    """
    Returns a list with instances of the available parser objects.
    """
    package_obj, plugins = get_plugins()
    parsers_objects = []
    for plugin in plugins:
        module_obj = getattr(package_obj, plugin)
        for elem in dir(module_obj):
            if elem != 'BaseParser':
                obj = getattr(module_obj, elem)
                if inspect.isclass(obj):
                    if issubclass(obj, BaseParser):
                        inst = obj()
                        parsers_objects.append(inst)
    return parsers_objects


def get_available_parsers():
    """
    Returns a list with available file formats for parsing.
    """
    parser_objects = get_parsers_instances()
    available_parsers = []
    for parser_obj in parser_objects:
        available_parsers.append(parser_obj.cl_desc())
    return available_parsers

