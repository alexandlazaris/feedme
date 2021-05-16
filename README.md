[![CircleCI](https://circleci.com/gh/alexandlazaris/feedme.svg?style=svg)](https://circleci.com/gh/alexandlazaris/feedme)

# feedme

- Create your player
- Try to stay alive
- Random events will cause you harm
- Better not lose ... your arm ...
- Every 3 seconds you level up!

`pip install -r requirements.txt`
`pytest tests/tests.py -v`
`python3 game/main.py`

## TODO:

- Add random enemy encounters
- If enemies have more attack than player, minus enemy attack from player heath. And vice-versa for player
- Add game over state if player health is 0
- create an event system, which triggers an event every nth second
- events include: nothing, enemy, lvlup
