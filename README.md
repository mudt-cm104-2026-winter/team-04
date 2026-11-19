# Fetch The Treat

## What this is

Fetch The Treat is a small quiz game about Git and GitHub. Loony the dog asks you, Max, multiple-choice questions about Git commands. A right answer earns Loony a treat. A wrong answer makes Loony sadder and then angrier.

The rules:

- Get **8 treats** and you win.
- **5 wrong answers** in total and Loony sadly leaves.
- **5 wrong answers in a row** and Loony gets so cross that she eats Max (cartoon style, no gore).
- You can ask Loony for **help 2 times** per game: she rules out one wrong answer.

The game runs in the browser. It is built with Python (FastAPI) and HTML templates (Jinja2). It uses no JavaScript.

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The game state is kept in memory: after a restart of the server, a new game starts.

## Team

| GitHub | Role |
|---|---|
| Matyyy3 | Game logic: questions, answers, help and endings (`app/questions.py`, `app/storage.py`) |
| geko-crypto | The page and the look: HTML, CSS, Max and Loony, animations |
| Daitaii-dev | The contract stub (routes in `app/main.py` and placeholder game state in `app/storage.py`), documentation, the issue board and the clean-up of issues and epics, pull request reviews and playtesting |

## How we work

- Every piece of work starts as an **issue** on our board. Issues are grouped in three epics: Frontend, Game logic, and Stub and documentation.
- One issue gets **one branch**, named after it (for example `54-complete-readme`), and **one pull request**.
- The pull request description has the sections What, Why and How to check, and says `Closes #n`.
- Nobody pushes to `main`. Every pull request needs **one approval** from another team member, and the author merges after the approval.
- Reviewers leave comments on the lines they mean. If something must change, they use **Request changes**, the author fixes it, and the reviewer approves.
- Every pull request adds one line to `CHANGELOG.md`.
- If two branches change the same lines, the second author solves the conflict on their laptop with `git fetch` and `git merge origin/main`.

## Sources

- 2026-11-04: course starter repository (FastAPI and Jinja2 template), used as the base of the app.

## Use of AI


- 2026-11-13: Claude , used by Daitaii-dev for some guidance on Git, GitHub and Python, and to draft the Max, Loony and office scene (SVG and CSS). Checked by running the game locally, and review by a teammate in the pull request.
- 2026-11-17: Claude , used by Matyyy3 for some guidance on Git, GitHub and Python,
- 2026-11-18: AI help for the improved visuals and stage (pull request #45), used by geko-crypto. Checked by running the game and by review in the pull request.
- 2026-11-18: Claude (Claude Code desktop app), used by Daitaii-dev for help with repo clean up and readme draft