class Film:
    def __init__(self, _id: int, _title: str) -> None:
        self._id = _id
        self._title = _title

    def setID(self, id: int) ->None:
        self._id = _id

    def setTitle(self, _title: str) ->None:
        self._title = _title

    def getID(self) ->int:
        return self.setID()
    
    def getTitle(self) ->str:
        return self.setTitle()
    
