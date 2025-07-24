from game.player import PlayerClass
from game.enemy import EnemyClass
    
def test_create_player_with_valid_stats():
    HEALTH = 10
    ATTACK = 13
    DEFENCE = 6
    player = PlayerClass("Player", HEALTH, ATTACK, DEFENCE)
    assert player.hp == HEALTH
    assert player.attack == ATTACK
    assert player.defence == DEFENCE

def test_create_enemy_with_valid_stats():
    HEALTH = 100
    ATTACK = 100
    DEFENCE = 100
    enemy = EnemyClass(HEALTH, ATTACK, DEFENCE)
    assert enemy.name is not None
    assert enemy.hp == HEALTH
    assert enemy.attack == ATTACK
    assert enemy.defence == DEFENCE

def test_player_can_level_up_once():
    HEALTH = 10
    ATTACK = 13
    DEFENCE = 6
    player = PlayerClass("Player", HEALTH, ATTACK, DEFENCE)
    current_level = player.level
    
    player.level_up()
    latest_level = player.level
    
    assert latest_level > current_level

def test_player_can_level_up_10_times():
    HEALTH = 10
    ATTACK = 13
    DEFENCE = 6
    player = PlayerClass("Player", HEALTH, ATTACK, DEFENCE)
    current_level = player.level
    
    for i in range(10):
        player.level_up()
        latest_level = player.level
        print (latest_level)
        assert latest_level > current_level