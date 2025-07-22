import tkinter as tk
from random import randint

def roll_dice():
    dice_result.set(f"Du hast eine {randint(1, 6)} gewürfelt!")

root = tk.Tk()
root.title("Monopoly")

# Spielfeld
canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()

# Beispiel eines Feldes
canvas.create_rectangle(1, 50, 150, 150, fill="lightblue", outline="black")
canvas.create_text(100, 100, text="Start", font=("Arial", 16))

# Schaltflächen und Status
dice_result = tk.StringVar()
dice_result.set("Würfeln, um zu starten!")

roll_button = tk.Button(root, text="Würfeln", command=roll_dice)
roll_button.pack()

result_label = tk.Label(root, textvariable=dice_result)
result_label.pack()

root.mainloop()
