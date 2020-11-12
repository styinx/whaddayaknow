import os
from os.path import join, realpath, normpath

from util.config import Config


def path(first: str, *other):
    return normpath(join(first, *other))


VERSION = '0.5.2'
USER_DIR = os.path.expanduser('~')
BASE_DIR = path(realpath(__file__), '..', '..')


ROLE_ADMIN = 'Admin'
ROLE_ORGANIZER = 'Organizer'
ROLE_QUIZ_MASTER = 'Quiz Master'
ROLES_ORGANIZER = [ROLE_ADMIN, ROLE_ORGANIZER]

EMOJI_OK = u'\U0001f44d'    # ':+1:'
EMOJI_DECLINE = u'\u274c'   # ':x:'


CONFIG = Config(path(BASE_DIR, 'config.json'))
KEYS = Config(path(BASE_DIR, 'keys.json'))
