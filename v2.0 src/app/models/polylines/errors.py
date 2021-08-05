__author__ = 'Cobbin'

class LineError(Exception):
    def __init__(self, message):
        self.message = message

class LineDontExistError(LineError):
    pass

class InvalidQuery(LineError):
    pass

