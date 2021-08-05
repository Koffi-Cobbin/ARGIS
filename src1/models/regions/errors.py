__author__ = 'Cobbin'

class RegionError(Exception):
    def __init__(self, message):
        self.message = message

class RegionDontExistError(RegionError):
    pass

class InvalidQuery(RegionError):
    pass

