import random

# Variablen initialisieren
laengePw = 0
pw = ""

# Loop durch die Passwortlänge
while laengePw < 10:
    # Random Zahl generieren
    random_num = random.randint(0,127)
    # Generierte Zahl abprüfen ob zwischen 32 und 127
    if random_num > 32 and random_num < 127:
        # if true hänge ASCII Zeichen an Stelle der generierten Zahl an das Passwort
        zeichen = chr(random_num)
        pw += zeichen
        laengePw += 1

print(pw)