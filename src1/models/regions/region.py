

class Region():
    def __init__(self, name, towns, _id=None):
        self._id = None if _id is None else _id
        self.name = name 
        self.towns = [] #A list of town ids in this region