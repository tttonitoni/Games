import tkinter as tk
from tkinter import messagebox

def print_leck_eier():
    messagebox.showerror("error", "leck eier")

if __name__ == "__main__":
    fenster = tk.Tk()

    # Titel des Fensters
    fenster.title("Toni.T")
    # Maße des Fensters
    fenster.geometry("400x300")

    Knopf = tk.Button(fenster, text = "Leck eier",command = print_leck_eier)
    Knopf.pack(pady=10)

    fenster.mainloop()