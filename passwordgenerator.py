import random

def generate_password():
    # Initialisiere Passwort als Liste und Ascii Set
    pw = []
    # Ascii character von 33 bis 127
    characters = "".join(chr(char) for char in range(33, 127))

    # Passwort Liste wird erweitert um einen random Eintrag unserer character Liste
    for _ in range(10):
        pw.append(random.choice(characters))

    # Return der Liste als String
    return "".join(pw)


# Print zur Konsole
print(generate_password())