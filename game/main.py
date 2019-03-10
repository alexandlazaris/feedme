import threading
from player import PlayerStart as newPlayerStart

newPlayer = newPlayerStart("Alexander", 10, 3, 3)

def main():
    threading.Timer(3.0, main).start()
    newPlayer.lvlup()
    newPlayer.damageHealth()

main()