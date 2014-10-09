
class DictionaryException(Exception):
    """
    Exception raised when dictionary from dictionraies.py not found.
    """

class WrongArgumentValue(Exception):
    def init(self, message, errors):
        Exception.__init__(self, message)
        self.errors = errors