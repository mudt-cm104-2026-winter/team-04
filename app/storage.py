"""Where the game state is kept.

For now: placeholder values, so the page can be built while the real game
rules are still being written. The rest of the app only uses the functions
below, so main.py does not change when the real logic replaces the placeholders.
"""

def get_state():
    return {
        "question":"Which command shows what has changed right now?",
        "options":["git status", "git clone", "git remote"],
        "removed_option":None, "treats": 0, "wrong": 0, "streak": 0, "mood":0,
        "mood_name":"happy", "helps_left": 2, "message": "", "game_over": False,
        "ending":""
    }

def answer(choice):
    pass

def help_used():
    pass

def restart():
    pass


