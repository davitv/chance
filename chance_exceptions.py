
class WrongArgumentValue(Exception):
    def init(self, message, errors):
        Exception.__init__(self, message)
        self.errors = errors