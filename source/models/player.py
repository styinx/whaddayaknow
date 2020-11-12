class Player:
    def __init__(self, player_id: int):
        self._id = player_id
        self._points = 0

    @property
    def id(self):
        return self._id

    @property
    def points(self):
        return self._points
