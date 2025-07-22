[![CircleCI](https://circleci.com/gh/alexandlazaris/feedme.svg?style=svg)](https://circleci.com/gh/alexandlazaris/feedme)

# feedme

- Create your player
- Every 3 seconds an event will trigger (walking, nothing or enemy encounter)
- Gameover when HP is 0
- Player lvl + HP are hidden during gameplay
- Enemy progressively gets stronger as player lvls up

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pytest tests/tests.py -v`
5. `python3 game/main.py`

## TODO:

- overlay enemy + player stats in the 1 chart
- link to chart in CLI output
- change HITS + DMG to ATTACK + DEFENCE for both
- different colours for both
- add enemy name in top right