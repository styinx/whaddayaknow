class Question:
    class TYPE:
        NORMAL, NORMAL_IMAGE, NORMAL_SOUND, MULTIPLE_CHOICE, ORDERED = range(0, 5)

    def __init__(self, question_type: int, text: str):
        self._type = question_type
        self._text = text

    @property
    def type(self):
        return self._type

    @property
    def text(self):
        return self._text
