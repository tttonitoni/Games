# Kosten mit 19% stuern
# Toni.T 26.9.24


print("Mengen Preis mit und ohne steuern Berechner")
print("---------------------------------------------")

anzahl = float(input("Anzahl der produkte: "))
preis = float(input("und der preis von einem produkt: "))
gew = float(input("Wie viel gewin wollen sie machen in %: "))
    
print("---------------------------------------------")

a_preis = preis * anzahl    # Insgesamter Preis

PlusP = a_preis/100*19  # 19% steuern hinzufügenc
a_PlusP = a_preis + PlusP

G_Plus = a_PlusP/100*gew
a_plusG = a_PlusP + G_Plus


print(f"Der Preis ohne steuern ist {a_preis}")
print(f"Der Preis mit steuern {a_PlusP}")
print(f"Der preis mit {int(gew)}% gewinn beträgt {a_plusG}")
print("---------------------------------------------")
input()