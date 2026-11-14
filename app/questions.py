QUESTIONS = [
    {
        "question": "Which command shows the history of commits?",
        "options": ["git log", "git push", "git init"],
        "answer": 0,
    },
    {
        "question": "Which command sends your commits to GitHub?",
        "options": ["git add", "git push", "git status"],
        "answer": 1,
    },
    {
        "question": "What does git add do?",
        "options": [
            "Saves to GitHub",
            "Deletes a file",
            "Puts changes into the staging area",
        ],
        "answer": 2,
    },
    {
        "question": "Which key do you give to GitHub for SSH?",
        "options": ["The private key", "The public key (.pub)", "Your password"],
        "answer": 1,
    },
    {
        "question": "Which command creates and switches to a new branch?",
        "options": ["git merge name", "git commit -c name", "git switch -c name"],
        "answer": 2,
    },
    {
        "question": "What is a pull request?",
        "options": [
            "A request to merge your branch, with a review",
            "A command that deletes main",
            "A GitHub password reset",
        ],
        "answer": 0,
    },
    {
        "question": "Which command shows what has changed right now?",
        "options": ["git remote", "git clone", "git status"],
        "answer": 2,
    },
    {
        "question": "What must you never do on a shared branch?",
        "options": ["git push --force", "git status", "git log"],
        "answer": 0,
    },
    {
        "question": "Which command copies a repository from GitHub to your machine?",
        "options": ["git branch", "git clone", "git diff"],
        "answer": 1,
    },
    {
        "question": "What does git commit do?",
        "options": [
            "Saves a snapshot of the staged changes",
            "Uploads to GitHub",
            "Deletes the last file",
        ],
        "answer": 0,
    },
    {
        "question": "Which command fetches new commits from GitHub and merges them?",
        "options": ["git rm", "git pull", "git init"],
        "answer": 1,
    },
    {
        "question": "What does a .gitignore file do?",
        "options": [
            "Tells Git which files not to track",
            "Hides your password",
            "Deletes old branches",
        ],
        "answer": 0,
    },
    {
        "question": "Which command starts a new Git repository?",
        "options": ["git new", "git init", "git start"],
        "answer": 1,
    },
    {
        "question": "Why do we use a pull request?",
        "options": [
            "So teammates can review before merging",
            "To erase the history",
            "To change a password",
        ],
        "answer": 0,
    },
    {
        "question": "A merge conflict is fixed. What next?",
        "options": [
            "git add the file, then commit",
            "git push --force",
            "Delete the repository",
        ],
        "answer": 0,
    },
]
RIGHT_MESSAGES = [
    "Nice work!",
    "Tadaaaaaa",
    "Right! A treat for the good boy!",
    "Good one!",
    "Correct! Your Git knowledge is growing fast.",
]
WRONG_MESSAGES = [
    "Wrong! Loony looks a bit sad...",
    "*sniff* Wrong! Aww, Loony is really sad.",
    "*growls* Wrong! Loony is getting grumpy...",
    "*GRRR!* Wrong! Careful! Loony is furious!",
    "*FURIOUS ROAR!* Game over. Loony has had enough!",
]
