import os
import platform

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
DARK_PURPLE = '\033[35m'
CYAN = "\033[96m"
WHITE = '\033[97m'  # Helles Weiß
DARK_GRAY = '\033[90m'  # Dunkles Grau
RESET = "\033[0m"  # Zurück zur Standardfarbe
LIGHT_GRAY = '\033[37m'

def star():
    clear_console()

    text = f"""
    {RED}
                                             ______             __   _    __
                                            /_  __/___   _____ / /_ | |  / /                               
                                             / /  / _ \ / ___// __/ | | / / 
                                            / /  /  __/(__  )/ /_ _ | |/ /  
                                           /_/   \___//____/ \__/(_)|___/   
    {WHITE}
                                                                                                                                           
    """

    print(text)

def info ():
    print(f"{RED}                  1 {WHITE}Kosten berechen       {RED}3 {WHITE}Zahlen Raten")
    print(f"{RED}                  2 {WHITE}Slot Maschin   ")
    print()

def usr_input():
    inp = (f"{RED}-/> {WHITE}")
    zahl = int(input(inp))
    return zahl

def clear_console():
    # Betriebssystem überprüfen
    if platform.system() == "Windows":
        os.system("cls")  # Für Windows
    else:
        os.system("clear")  # Für Linux und macOS
