[![CircleCI](https://circleci.com/gh/alexandlazaris/feedme.svg?style=svg)](https://circleci.com/gh/alexandlazaris/feedme)

# feedme

- Create your player
- Every 3 seconds an event will trigger (walking, nothing or enemy encounter)
- Gameover when HP is 0
- Player lvl + HP are hidden during gameplay
- Enemy progressively gets stronger as player lvls up

`pip install -r requirements.txt`

`pytest tests/tests.py -v`

`python3 game/main.py`

## TODO:

- Add random enemy encounters > done
- If enemies have more attack than player, minus enemy attack from player heath. And vice-versa for player
- Add game over state if player health is 0 > done
- create an event system, which triggers an event every nth second > done
- events include: nothing, enemy, lvlup > done
- host results on a webserver, run python3 -m webbrowser -t "webpage" to show end results
- refactor enemy & player into a base class
- need to have nextLvl exp progressively increase higher with each lvl
- find a better formula to gain exp based on lvl
- generate a new enemy object based off character stats
- get player to attack enemy
