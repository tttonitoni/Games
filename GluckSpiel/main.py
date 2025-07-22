from farbenGrafiken import LogoPrint,Logo
from funktionen import *

Geld = 50
spiel = 0

main = True
while main:
    clear_console()
    coice = Menu(Geld)

    if coice == "1":
        Geld, game = Startgame(Geld,spiel)
        spiel += game
        


    elif coice == "2":
        main = False