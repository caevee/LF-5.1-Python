import random

def generateKundennummer():
    # Deklariere und initialisiere die Kundennummer als Liste
    kundennummer = [""] * 12
    quersumme = 0

    # Befuelle erste zwei Stellen direkt mit KD
    kundennummer[0] = "K"
    kundennummer[1] = "D"

    # Befuelle Stellen 3-10 mit zufaelligen Zahlen
    for i in range(2, 10):
        randomNum = random.randint(1,9)
        quersumme += randomNum
        kundennummer[i] = str(randomNum)

    
    if len(str(quersumme)) == 1:
        quersumme = list("0" + str(quersumme))
    else:
        quersumme = list(str(quersumme))

    kundennummer[10] = quersumme[0]
    kundennummer[11] = quersumme[1]
    
    
    # Returne Kundennummer als String
    return "".join(kundennummer)

print(generateKundennummer())