from .. import player

testPlayer = player.PlayerStart("Alexander", 10, 10, 10)

def test_basic():
    assert 1 == 1

def test_playerHealthIsSet():
    assert testPlayer.getHealthValue() != 0
