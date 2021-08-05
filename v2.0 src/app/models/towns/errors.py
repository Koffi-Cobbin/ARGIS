__author__ = 'Cobbin'

class TownError(Exception):
    def __init__(self, message):
        self.message = message

class TownDontExistError(TownError):
    pass

class InvalidQuery(TownError):
    pass

