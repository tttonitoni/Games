import os
import hashlib

# Funktion zum Berechnen des Hashwerts einer Datei
def calculate_file_hash(file_path, chunk_size=8192):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

# Funktion zum Finden doppelter Dateien in einem Verzeichnis
def find_duplicates(directory):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)

            # Prüfen, ob der Hash bereits existiert (also eine doppelte Datei gefunden wurde)
            if file_hash in hashes:
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path

    return duplicates

# Hauptfunktion zur Anzeige der Duplikate
def main():
    directory = input("Gib das Verzeichnis an, das nach Duplikaten durchsucht werden soll: ")
    duplicates = find_duplicates(directory)

    if duplicates:
        print("\nGefundene Duplikate:")
        for duplicate, original in duplicates:
            print(f"Duplikat: {duplicate} | Original: {original}")
    else:
        print("Keine Duplikate gefunden.")

# Starte das Tool
if __name__ == "__main__":
    main()
