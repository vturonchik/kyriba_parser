class BaseParser(object):

    def cl_desc(self):
        """
        Must return a string with the file format to call the appropriate parser.
        """
        raise NotImplementedError

    def help_message(self):
        """
        Must return a string describing the format of the output.
        """
        raise NotImplementedError

    def parser(self, path):
        """
        The input receives the path to the file for parsing.
        Must return a list with the processed data for output in the main program.
        """
        raise NotImplementedError
