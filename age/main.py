import sys
import time
import os


def clear():
    os.system('cls')

def printstrt():
    print("Alter Rater")

def loading_bar(total_steps, delay=0.1):
    for i in range(total_steps + 1):
        # Calculate the percentage of completion
        percent = (i / total_steps) * 100
        # Determine how many "#" symbols to display
        bar_length = int((i / total_steps) * 30)  # Adjust the 30 for the bar length
        bar = "#" * bar_length + "-" * (30 - bar_length)
        # Print the loading bar with percentage, carriage return to overwrite the line
        sys.stdout.write(f"\r|{bar}| {percent:.2f}%")
        sys.stdout.flush()
        # Delay to simulate loading
        time.sleep(delay)

    # Print a final message after the loading is complete, adding a new line
    sys.stdout.write("\nLoading complete!\n")

# Run the loading bar for 50 steps
# loading_bar(50)

print()
age  = input("-> Wie alt bist du?: ")
clear()
print()
print("-> Sucht im Interne: ")
loading_bar(50)
time.sleep(1)
clear()
print()
print(f"-> Nach suche im Internet haben herausgefunden das du {age} jahre alt bist")
input()
