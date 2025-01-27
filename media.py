contatore = 0
somma = 0
numero = input ("dammi un numero")

while numero != "fine":
      contatore += 1
      somma += float(numero)
      numero = input ("inserire il prossimo numero")
print ("La tua media è: " , somma/contatore)



