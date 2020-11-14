from models.player import Player


class Team:
    def __init__(self, role, team_id: int):
        self._id = team_id
        self._role = role
        self._members = set()
        self._points = 0

    # Properties

    @property
    def members(self):
        return self._members

    @property
    def points(self):
        return self._points

    # Public

    def add(self, member: Player):
        self._members.add(member)

    def remove(self, member: Player):
        self._members.remove(member)
