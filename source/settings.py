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

COLOR_QUIZ_MASTER = 0xCCCC00

EMOJI_OK = u'\U0001f44d'        # ':+1:'
EMOJI_ACCEPT = u'\u2705'        # ':white_check_mark:'
EMOJI_DECLINE = u'\u274E'       # ':negative_squared_cross_mark:'
EMOJI_FORWARD = u'\u27a1'       # ':arrow_right:'
EMOJI_BACKWARD = u'\u2b05'      # ':arrow_left:'
EMOJI_PLAY_PAUSE = u'\u23EF'    # ':play_pause:'
EMOJI_STOP = u'\u23F9'          # ':stop_button:'
EMOJI_STOPWATCH = u'\u23F1'     # ':stopwatch:'
EMOJI_ONE = u'\u0031\u20E3'       # ':one:'1️
EMOJI_TWO = u'\u0032\u20E3'           # ':two:'
EMOJI_THREE = u'\u0033\u20E3'         # ':three:'
EMOJI_FOUR = u'\u0034\u20E3'          # ':four:'
EMOJI_FIVE = u'\u0035\u20E3'          # ':five:'
EMOJI_SIX = u'\u0036\u20E3'           # ':six:'
EMOJI_SEVEN = u'\u0037\u20E3'         # ':seven:'
EMOJI_EIGHT = u'\u0038\u20E3'         # ':eight:'
EMOJI_A = u'\U0001F1E6'         # ':regional_indicator_a:'
EMOJI_B = u'\U0001F1E7'         # ':regional_indicator_b:'
EMOJI_C = u'\U0001F1E8'         # ':regional_indicator_c:'
EMOJI_D = u'\U0001F1E9'         # ':regional_indicator_d:'
EMOJI_TEAM = [EMOJI_ONE, EMOJI_TWO, EMOJI_THREE, EMOJI_FOUR, EMOJI_FIVE, EMOJI_SIX, EMOJI_SEVEN, EMOJI_EIGHT]

CONFIG = Config(path(BASE_DIR, 'config.json'))
KEYS = Config(path(BASE_DIR, 'keys.json'))
