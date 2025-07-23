[![CircleCI](https://circleci.com/gh/alexandlazaris/feedme.svg?style=svg)](https://circleci.com/gh/alexandlazaris/feedme)

# feedme - CLI RPG

Game details:

- Name your player & duke it out with your chosen enemy
- Every turn, you'll either rest, gain XP or get WHACKED
- Gameover when your HP is 0
- Both you and enemy stats progressively increase the longer the game goes on

To start:

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pytest tests/tests.py -v`
5. `python3 game/main.py`

Radar chart:

Whilst playing you'll see a lovely radar chart showing both your & the enemy stats. This chart live updates as the game plays out. See who can reach level 100 first!

> [!IMPORTANT]
> Enemy names are randomly generated each run using Faker library. There are no enemies here, only fun times.

![img](./rpg_radar.png)