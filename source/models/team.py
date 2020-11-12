from models.player import Player


class Team:
    def __init__(self):
        self._members = set()
        self._points = 0

    @property
    def members(self):
        return self._members

    @property
    def points(self):
        return self._points

    def add(self, member: Player):
        self._members.add(member)

    def remove(self, member: Player):
        self._members.remove(member)
