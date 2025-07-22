# B(n) Berechnen
# Toni.T 1.10.24

# Eingabe 
B_null = float(input("Was ist B(0): "))
b = float(input("Was ist der faktor(b): "))
n = float(input("Was ist n: "))

# Rechnung
z = 0

while n+1 != z:
    BvN = B_null*b**z
    print(f"B({z}) = {BvN}")
    z = z + 1