To write your own parser from scratch, you need:
1. In the plugins folder, create a new file with the extension .py
2. Import the class with a basic parser (from base_parser import BaseParser)
3. Create your own class and inherit from the BaseParser class
4. Override methods:
  - 1. cl_desc() to output the file format on the command line and select the correct parser after user input;
  - 2. help_message() for output in the command prompt with the format of the output data;
  - 3. parser(path) the input of which is passed the path to the file for parsing. And the output returns a list with the data to output;
