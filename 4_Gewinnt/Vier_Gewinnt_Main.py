# 4 Gewinnt nachbauen
# Toni.T 29.10.24

from Vier_Gewinnt_funktionen import *

# Main loop
main = True
while main:
    PrintMenue()
    coice = input("Geben sie eine zahl ein(1-2): ")
    if coice == "1":
        vier_gewinnt()
    
    elif coice == "2":
        main = False