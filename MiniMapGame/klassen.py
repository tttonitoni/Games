import random

class Weapon:
    def __init__(self, name, damage, price=0):
        self.name = name
        self.damage = damage
        self.price = price

class Entity:
    def __init__(self, name, strength, health, weapon=None, money=0):
        self.name = name
        self.strength = strength
        self.health = health
        self.max_health = health
        self.weapon = weapon
        self.inventory = []
        self.money = money
        self.special_used = False
        self.status_effects = []

    def attack(self, target):
        if not self.weapon:
            print(f"{self.name} hat keine Waffe!")
            return

        hit_chance = random.random()
        if hit_chance < 0.2:
            print(f"{self.name} verfehlt den Angriff!")
            return

        is_critical = random.random() < 0.15
        damage = self.weapon.damage * self.strength
        if is_critical:
            damage *= 2
            print(f"Kritischer Treffer!")

        target.health -= damage
        target.health = max(target.health, 0)
        print(f"{self.name} macht {round(damage, 1)} Schaden an {target.name}.")

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.health += heal_amount
        self.health = min(self.health, self.max_health)
        print(f"{self.name} heilt sich um {heal_amount} Leben.")

    def use_special(self, target):
        if self.special_used:
            print(f"{self.name} hat seine Spezialfähigkeit bereits verwendet!")
            return
        print(f"{self.name} setzt seine Spezialfähigkeit ein!")
        damage = self.weapon.damage * self.strength * 2.5
        target.health -= damage
        target.health = max(target.health, 0)
        print(f"{self.name} verursacht {round(damage, 1)} Spezialschaden an {target.name}!")
        self.special_used = True

    def show_stats(self):
        weapon_name = self.weapon.name if self.weapon else "Keine"
        print(f"Leben: {self.health}/{self.max_health} | Stärke: {self.strength} | Waffe: {weapon_name} | Geld: {self.money}$")

    def health_bar(self, width=20):
        ratio = self.health / self.max_health
        filled = int(ratio * width)
        empty = width - filled
        return f"[{ '█' * filled }{ '-' * empty }] {int(self.health)}/{self.max_health}"

    def show_inventory(self):
        if not self.inventory:
            print("Inventar ist leer.")
            return
        for idx, item in enumerate(self.inventory, start=1):
            print(f"{idx}. {item.name}")
        try:
            index = int(input("Welche Waffe möchtest du auswählen (Index)? >>> ")) - 1
            if 0 <= index < len(self.inventory):
                self.weapon = self.inventory[index]
                print(f"Waffe gewechselt zu: {self.weapon.name}")
            else:
                print("Ungültiger Index!")
        except ValueError:
            print("Ungültige Eingabe!")

    def shop(self, weapons):
        print("Willkommen im Shop!\n1. Waffen kaufen")
        if input(">>> ") != "1":
            return
        for i, weapon in enumerate(weapons):
            status = "Gekauft" if weapon in self.inventory else f"Preis: {weapon.price}$"
            print(f"{i+1}. {weapon.name} ({status})")

        print(f"Du hast {self.money}$")
        try:
            index = int(input("Welche Waffe möchtest du kaufen (Index)? >>> ")) - 1
            selected = weapons[index]
            if selected in self.inventory:
                print("Diese Waffe besitzt du bereits.")
            elif self.money >= selected.price:
                self.money -= selected.price
                self.weapon = selected
                self.inventory.append(selected)
                print(f"Du hast {selected.name} gekauft und ausgerüstet!")
            else:
                print("Nicht genug Geld!")
        except (ValueError, IndexError):
            print("Ungültige Auswahl!")


def fight(player, enemy):
    player.health = player.max_health
    enemy.health = enemy.max_health
    player.special_used = False
    enemy.special_used = False
    round_num = 1

    while True:
        print(f"\n--- Runde {round_num} ---")
        print(f"{player.name}: {player.health_bar()}")
        print("Was möchtest du tun?\n1. Angreifen\n2. Heilen\n3. Spezial\n4. Aufgeben")
        choice = input(">>> ")

        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.heal()
        elif choice == "3":
            player.use_special(enemy)
        elif choice == "4":
            print("Du hast aufgegeben.")
            break
        else:
            print("Ungültige Eingabe!")
            continue

        if enemy.health <= 0:
            print("Du hast gewonnen!")
            player.money += 25
            break

        print(f"\n{enemy.name} ist am Zug...")
        print(f"{enemy.name}: {enemy.health_bar()}")

        if enemy.health < 25 and not enemy.special_used:
            enemy.use_special(player)
        elif enemy.health < enemy.max_health * 0.3 and random.random() < 0.5:
            enemy.heal()
        else:
            enemy.attack(player)

        if player.health <= 0:
            print("Du hast verloren.")
            player.money += 5
            break

        round_num += 1


def create_character(weapons):
    name = input("Wie möchtest du heißen? ")
    choice = input("Möchtest du stärker (1) sein oder mehr Leben (2) haben? ")
    if choice == "1":
        strength = round(random.uniform(1.5, 2.5), 1)
        health = round(100 / strength)
    else:
        health = random.randint(130, 170)
        strength = round(random.uniform(1.1, 1.5), 1)

    player = Entity(name, strength, health, weapon=weapons[0])
    print(f"{player.name} hat {health} Leben und {strength} Stärke.")
    return player

# Spielstart
weapons_list = [
    Weapon("Holz Schwert", 5, price=0),
    Weapon("Stein Schwert", 9, price=10),
    Weapon("Eisen Schwert", 14, price=50),
    Weapon("Diamant Klinge", 20, price=100),
    Weapon("Flammenwerfer", 30, price=150),
    Weapon("Laser Schwert", 45, price=250)
]

enemies = [
    Entity("Eichel Lecker", 1.0, 40, Weapon("Eichel", 4)),
    Entity("Ohren Kneifer", 1.1, 75, Weapon("Zange", 6)),
    Entity("Herr Braun", 1.3, 110, Weapon("Brille", 9)),
    Entity("Feuer Golem", 1.6, 160, Weapon("Feuerfaust", 13)),
    Entity("Cyberschatten", 2.0, 180, Weapon("Nano-Klinge", 16)),
    Entity("Dr. Stahlfaust", 2.2, 220, Weapon("Stahlfaust", 20))
]

player = create_character(weapons_list)

while True:
    print(f"\nWillkommen zum Kampf-Simulator, {player.name}! Was möchtest du tun?")
    print("1. Kämpfen\n2. Status anzeigen\n3. Shop\n4. Inventar\n5. Beenden")
    action = input(">>> ")

    if action == "1":
        enemy = random.choice(enemies)
        print(f"Du kämpfst gegen {enemy.name}, der die Waffe {enemy.weapon.name} hat.")
        fight(player, enemy)
    elif action == "2":
        player.show_stats()
    elif action == "3":
        player.shop(weapons_list)
    elif action == "4":
        player.show_inventory()
    elif action == "5":
        print("Auf Wiedersehen!")
        break
    else:
        print("Ungültige Eingabe!")