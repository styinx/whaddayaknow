import re
from settings import CONFIG

ID = 0
LANG = CONFIG.get('language')


def text_id():
    global ID
    ID += 1
    return ID


CHANNEL_ORGA = text_id()
CHANNEL_SETUP = text_id()
CHANNEL_LOBBY = text_id()

NEW_QUIZ = text_id()


TEXTS = {
    'de': {
        CHANNEL_ORGA: 'Organisation',
        NEW_QUIZ: str(
            'Ein neues "{}" Quiz wurde gestarted. Bitte reagiere mit dem :+1: emoji um teilzunehmen.\n'
            '__**Teilnehmer:**__\n'
            '{}'
        )
    },
    'en': {
        CHANNEL_ORGA: 'Organization',
        CHANNEL_SETUP: 'setup',
        CHANNEL_LOBBY: 'lobby',
        NEW_QUIZ: str(
            'A new "{}" quiz was started. Please react with the :+1: emoji to participate. \n'
            '__**Participants:**__\n'
            '{}'
        ),
    },
}


def text(_id: int):
    if _id in TEXTS[LANG]:
        return TEXTS[LANG][_id]
    return TEXTS['en'][_id]


def idfy(t: str):
    return re.sub(r'\s', '-', t)


def i(t: str):
    return '*{0}*'.format(t)


def b(t: str):
    return '**{0}**'.format(t)


def u(t: str):
    return '__{0}__'.format(t)


def s(t: str):
    return '~~{0}~~'.format(t)


def c(t: str):
    return '`{0}`'.format(t)


def cb(t: str):
    return '```{0}```'.format(t)
