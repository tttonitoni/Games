from funktionen import Feld

spielbrett = [
    Feld("Los", "Start", preis=0),
    Feld("Badstraße", "Straße", "Braun", preis=60, miete=[2, 10, 30, 90, 160, 250], Hauskosten=50),
    Feld("Ereignisfeld", "Ereignis"),
    Feld("Turmstraße", "Straße", "Braun", preis=60, miete=[4, 20, 60, 180, 320, 450], Hauskosten=50),
    Feld("Einkommenssteuer", "Spezial", preis=200),
    Feld("Südbahnhof", "Bahnhof", "Schwarz", preis=200, miete=[25, 50, 100, 200]),
    Feld("Chausseestraße", "Straße", "Hellblau", preis=100, miete=[6, 30, 90, 270, 400, 550], Hauskosten=50),
    Feld("Ereignisfeld", "Ereignis"),
    Feld("Elisenstraße", "Straße", "Hellblau", preis=100, miete=[6, 30, 90, 270, 400, 550], Hauskosten=50),
    Feld("Poststraße", "Straße", "Hellblau", preis=120, miete=[8, 40, 100, 300, 450, 600], Hauskosten=50),
    Feld("Gefängnis", "Spezial"), # richtig
    Feld("Seestraße", "Straße", "Pink", preis=140, miete=[10, 50, 150, 450, 625, 750], Hauskosten=100),
    Feld("Elektizitätwerk", "Straße", "Werk", preis=150, miete=[4,10]),
    Feld("Hafenstraße", "Straße", "Pink", preis=140, miete=[10, 50, 150, 450, 625, 750], Hauskosten=100),
    Feld("Neue Straße", "Straße", "Pink", preis=160, miete=[12, 60, 180, 500, 700, 900], Hauskosten=100),
    Feld("Westbahnhof", "Bahnhof", "Schwarz", preis=200, miete=[25, 50, 100, 200]),
    Feld("Münchner Straße", "Straße", "Orange", preis=180, miete=[14, 70, 200, 550, 750, 950], Hauskosten=100),
    Feld("Gemeinschaftsfeld", "Gemeinschaft"),
    Feld("Wiener Straße", "Straße", "Orange", preis=180, miete=[14, 70, 200, 550, 750, 950], Hauskosten=100),
    Feld("Berliner Straße", "Straße", "Orange", preis=200, miete=[16, 80, 220, 600, 800, 1000], Hauskosten=100),
    Feld("Frei Parken", "Spezial"),
    Feld("Theaterstraße", "Straße", "Rot", preis=220, miete=[18, 90, 250, 700, 875, 1050], Hauskosten=150),
    Feld("Ereignisfeld", "Ereignis"),
    Feld("Museumstraße", "Straße", "Rot", preis=220, miete=[18, 90, 250, 700, 875, 1050], Hauskosten=150),
    Feld("Opernplatz", "Straße", "Rot", preis=240, miete=[20, 100, 300, 750, 925, 1100], Hauskosten=150),
    Feld("Nordbahnhof", "Bahnhof", "Schwarz", preis=200, miete=[25, 50, 100, 200]),
    Feld("Lessingstraße", "Straße", "Gelb", preis=260, miete=[22, 110, 330, 800, 975, 1150], Hauskosten=150),
    Feld("Schillerstraße", "Straße", "Gelb", preis=260, miete=[22, 110, 330, 800, 975, 1150], Hauskosten=150),
    Feld("Wasserwerk", "Straße", "Werk", preis=150, miete=[4, 10]),
    Feld("Goethestraße", "Straße", "Gelb", preis=280, miete=[24, 120, 360, 850, 1025, 1200], Hauskosten=150),
    Feld("Gehe ins Gefängnis", "Spezial"),
    Feld("Rathausplatz", "Straße", "Grün", preis=300, miete=[26, 130, 390, 900, 1100, 1275], Hauskosten=200),
    Feld("Hauptstraße", "Straße", "Grün", preis=300, miete=[26, 130, 390, 900, 1100, 1275], Hauskosten=200),
    Feld("Gemeinschaftsfeld", "Gemeinschaft"),
    Feld("Bahnhofstraße", "Straße", "Grün", preis=320, miete=[28, 150, 450, 1000, 1200, 1400], Hauskosten=200),
    Feld("Hauptbahnhof", "Bahnhof", "Schwarz", preis=200, miete=[25, 50, 100, 200]),
    Feld("Ereignisfeld", "Ereignis"),
    Feld("Parkstraße", "Straße", "Dunkelblau", preis=350, miete=[35, 175, 500, 1100, 1300, 1500], Hauskosten=200),
    Feld("Luxussteuer", "Spezial", preis=100),
    Feld("Schlossallee", "Straße", "Dunkelblau", preis=400, miete=[50, 200, 600, 1400, 1700, 2000], Hauskosten=200)
]

# Beispiel für eine Datenstruktur, die die Straßen nach Farbgruppen organisiert
farbgruppen = {
    "Braun": ["Badstraße", "Turmstraße"],
    "Hellblau": ["Chausseestraße", "Elisenstraße", "Poststraße"],
    "Pink": ["Seestraße", "Hafenstraße", "Neue Straße"],
    "Orange": ["Münchner Straße", "Wiener Straße", "Berliner Straße"],
    "Rot": ["Theaterstraße", "Museumstraße", "Opernplatz"],
    "Gelb": ["Lessingstraße", "Schillerstraße", "Goethestraße"],
    "Grün": ["Rathausplatz", "Hauptstraße", "Bahnhofstraße"],
    "Dunkelblau": ["Parkstraße", "Schlossallee"],
    "Schwarz": ["Haupbahnhof", "Südbahnhof", "Westbahnhof", "Nordbahnof"],
    "Werk": ["Wasserwerk", "Elektrizitäswerk"]
}