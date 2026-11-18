"""Where the game state is kept.

For now: placeholder values, so the page can be built while the real game
rules are still being written. The rest of the app only uses the functions
below, so main.py does not change when the real logic replaces the placeholders.
"""

import random

from . import questions

WIN_TREATS = 8
MAX_WRONG = 5
MAX_STREAK = 5
START_HELPS = 2
MOOD_NAMES = ["happy", "a little sad", "so sad", "grumpy", "furious"]

_order = []
_position = 0
_options = []
_correct = 0
_treats = 0
_wrong = 0
_streak = 0
_helps_left = 0
_removed_option = None
_message = ""
_game_over = False
_ending = ""



def get_state():
    mood = min(_wrong, 4)
    return {
        "question": _order[_position]["question"],
        "options": list(_options),
        "removed_option": _removed_option,
        "treats": _treats,
        "wrong": _wrong,
        "streak": _streak,
        "mood": mood,
        "mood_name": MOOD_NAMES[mood],
        "helps_left": _helps_left,
        "message": _message,
        "game_over": _game_over,
        "ending": _ending,
    }


def answer(choice):
    global _treats, _wrong, _streak, _message, _game_over, _ending, _position
    
    if _game_over:
        return
    if choice not in (0, 1, 2):
        return 
    if choice==_removed_option:
        return 
    is_right =(choice==_correct)

    if is_right:
        _treats+=1
        _streak=0
        _message=random.choice(questions.RIGHT_MESSAGES)
    else:
        _wrong+=1
        _streak+=1
        _message=questions.WRONG_MESSAGES[min(_wrong, len(questions.WRONG_MESSAGES)) - 1]
   
    if _streak>=MAX_STREAK:
        _game_over=True
        _ending="eaten"
    elif _wrong>=MAX_WRONG:
            _game_over=True
            _ending="left"
    if _treats==WIN_TREATS:
        _game_over=True
        _ending="win"

    if _game_over==False:
        _position+=1
        _load_question()

def help_used():
    pass


def _load_question():
    #THIS FUNCTION IS LOADING AND SHUFFLING THE QUESTIONS
    global _options, _correct, _removed_option
    q = _order[_position]
    right_text = q["options"][q["answer"]]
    _options = list(q["options"])
    random.shuffle(_options)
    _correct = _options.index(right_text)
    _removed_option = None


def restart():
    # THIS FUNCTION IS RESTARTING ALL IRREGULATR VARIABLES
    global _treats, _wrong, _streak, _helps_left, _removed_option, _message, _game_over, _ending, _order, _position

    _treats = _wrong = _streak = 0
    _helps_left = START_HELPS
    _removed_option = None
    _message = ""
    _game_over = False
    _ending = ""
    _order = list(questions.QUESTIONS)
    random.shuffle(_order)
    _position = 0
    _load_question()


restart()
