class Quiz:
    def __init__(self, quiz_type: str):
        self._type = quiz_type

    @property
    def type(self):
        return self._type
