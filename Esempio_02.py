
valore = int(input("Inserisci la lunghezza"))
lettera = str(input("Inserisci una lettera"))
contatore = 1
for i in range (valore):
    i = (" " * valore + lettera * contatore)
    valore -= 1
    contatore += 2
    print(i)

