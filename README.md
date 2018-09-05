To write your own parser from scratch, you need:
1. To create a file with the extension .py
2. Import the class with a basic parser (from base_parser import BaseParser)
3. Create your own class and inherit from the BaseParser class
4. Override methods:
* cl_desc() to output the file format on the command line and select the correct parser after user input;
* help_message() for output in the command prompt with the format of the output data;
* parser(path) the input of which is passed the path to the file for parsing. And the output returns a list with the data to output;

To add a new directory with plugins:
1. In the settings.conf file, in the plugins_dir parameter, use comma to add the path to the directory with the plugins.
2. There must be a __init__.py file in the directory