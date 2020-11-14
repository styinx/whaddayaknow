import re
from settings import CONFIG

ID = 0
LANG = CONFIG.get('language')


def text_id():
    global ID
    ID += 1
    return ID


CHANNEL_CATEGORY = text_id()
CHANNEL_SETUP = text_id()
CHANNEL_LOBBY = text_id()

NEW_QUIZ = text_id()
QUIZ_MASTER = text_id()

TEXTS = {
    'de': {
        NEW_QUIZ: str(
            'Ein neues "{}" Quiz wurde gestarted. Bitte reagiere mit dem :+1: emoji um teilzunehmen.\n'
            'Um einem Team beizutreten reagiere mit der Nummer des Teams (:one:-:eight:).\n'
            '__**Teilnehmer:**__\n'
            '{}'
        )
    },
    'en': {
        CHANNEL_CATEGORY: 'Quiz',
        CHANNEL_SETUP:    'setup',
        CHANNEL_LOBBY:    'lobby',
        NEW_QUIZ:         str(
            'A new "{}" quiz was started. Please react with the :+1: emoji to participate. \n'
            'To join a team react with the number of the team (:one:-:eight:).\n'
            '__**Participants:**__\n'
            '{}'
        ),
        QUIZ_MASTER:      'Quiz Master'
    },
}


def text(_id: int):
    if _id in TEXTS[LANG]:
        return TEXTS[LANG][_id]
    return TEXTS['en'][_id]


def idfy(t: str):
    return re.sub(r'\s', '-', t)


def i(t: str):
    """
    italic
    """
    return '*{0}*'.format(t)


def b(t: str):
    """
    bold
    """
    return '**{0}**'.format(t)


def u(t: str):
    """
    underlined
    """
    return '__{0}__'.format(t)


def s(t: str):
    """
    strikethrough
    """
    return '~~{0}~~'.format(t)


def c(t: str):
    """
    code
    """
    return '`{0}`'.format(t)


def cb(t: str):
    """
    codeblock
    """
    return '```{0}```'.format(t)
