# Changelog

- The game page now shows the question, three answer buttons, the counters, Loony's mood and a help button (#22)
- The page now disables the answer ruled out by Loony's help and the help button when no helps are left (#24)
- The page now shows a game-over screen with a text for each of the three endings and a Play again button (#25)
- Max and Loony are now drawn with CSS, and Loony's look and animation change with his mood (#38)
- The page is restyled with a centered layout, stat bubbles and treat-style answer buttons (#29)
- The game-over scene now plays an animation for each ending: win, left and eaten (#41)
- Add game state, restart and real get_state() in storage.py(#39)
- Add answer(choice): right and wrong answers, win, left and eaten endings, and the next question (#42)
- Add help_used(): Loony rules out one wrong option per question, 2 helps per game, and the page now reloads at the bottom after help (#43)
- The game scene is now a drawn office with an SVG Max and Loony instead of CSS boxes, with the same mood and ending animations (#45)
- Mood now resets to happy on a win and goes to furious on a loss; during the game it never drops after a right answer (#48)
- Restyle the page: bigger title, square full-width buttons matching the question box, new button colours (#52)
- Fix formatting of the changelog line from #45 (#56)
<!-- Every pull request adds one line at the top of "Unreleased":
- what changed, in one sentence (#<pull request number>)
Example:
- Entries can be deleted (#7)
-->

## Unreleased

- Start from the repository template
