from bot.context import Context
from models.player import Player
from models.team import Team
from util.text import *


class Quiz:
    def __init__(self, quiz_type: str, quiz_master, team_size: int):
        self._type = quiz_type
        self._master = quiz_master
        self._team_size = team_size
        self._participants = set()
        self._teams = []

    # Properties

    @property
    def type(self) -> str:
        return self._type

    @property
    def master(self):
        return self._master

    @property
    def participants(self) -> set:
        return self._participants

    @property
    def teams(self) -> []:
        return self._teams

    # Public

    def add_participant(self, participant: Player):
        pass

    def remove_participant(self, participant: Player):
        pass

    def add_team(self, team: Team):
        pass

    def remove_team(self, team: Team):
        pass

    def participant_list(self) -> str:
        return ', '.join([Context.get_nick_or_name(user=p) for p in self._participants])

    def organization_text(self) -> str:
        return text(NEW_QUIZ).format(self._type, self.participant_list())
