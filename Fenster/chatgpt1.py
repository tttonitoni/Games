# Eigenes Fenster in Py
# Toni.T 13.10.24

import tkinter as tk
import time

def button_clicked():
    label.config(text="Button wurde geklickt!")

root = tk.Tk() # Hauptfenster
root.title("Fenster") # Fenster Name
root.geometry("400x300")# Fenstergröße setzen (Breite x Höhe)

# Ein Label hinzufügen
label = tk.Label(
    root, 
    text="Klick auf den Button!")
label.pack(pady=20)  # Automatisches Platzieren mit Abstand

# Einen Button hinzufügen
button = tk.Button(root, text="Klicken", command=button_clicked)
button.pack(pady=20)

# Fenster ausführen lassen
root.mainloop()