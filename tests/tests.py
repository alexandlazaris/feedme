from .. import player

HEALTH = 10
ATTACK = 13
DEFENCE = 6

def test_setupConstructPlayer():
    testPlayer = player.PlayerStart("Alexander", HEALTH, ATTACK, DEFENCE)
    return testPlayer

def test_playerHealthIsSet():
    assert test_setupConstructPlayer().getHealthValue() == HEALTH

def test_playerHealthIsNotAnotherValue():
    assert test_setupConstructPlayer().getHealthValue() != 999

def test_playerAttackIsSet():
    assert test_setupConstructPlayer().getAttackValue() == ATTACK

def test_playerDefenceIsSet():
    assert test_setupConstructPlayer().getDefenceValue() == DEFENCE
