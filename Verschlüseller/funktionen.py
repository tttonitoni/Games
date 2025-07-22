# Funktionen für main

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    logo()
    print("1. Verschlüsseln")
    print("2. Entschlüsseln")
    print("")

def logo():
    text = """
     ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
    print(text)

def verschlüseler(text):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
    verschlüselter_text = [""] * len(text)

    for index in range(len(text)):
        for i in range(len(alphabet)):
            if text[index] == alphabet[i]:
                i = i + 3
                verschlüselter_text[index] = alphabet[i]
                break
    
    return verschlüselter_text

def entverschlüseler(text):
    alphabet2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
    verschlüselter_text = [""] * len(text)

    for index in range(len(text)):

        for i in range(len(alphabet2)):
            if text[index] == alphabet2[i]:
                i = i - 3
                verschlüselter_text[index] = alphabet2[i]
                break

    return verschlüselter_text