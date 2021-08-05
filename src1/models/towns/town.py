
class Town():
    def __init__(self, name, polylines, _id=None):
        self._id = None if _id is None else _id
        self.name = name 
        self.polylines = [] #A list of polyline ids in this town