

class Polyline():
    def __init__(self, town_id, coordinates, _id=None):
        self._id = None if _id is None else _id
        self.town_id = town_id
        self.coordinates = coordinates

    def getCoordinates(data):
        lst = re.findall('\(.*?\)', data) 
        return lst