import matplotlib.pyplot as plt

# Dati di esempio: ore (x) e temperatura (y) in gradi Celsius
ore = [8, 9, 10, 11, 12, 13, 14, 15, 16]
temperatura = [15, 16, 18, 19, 20, 21, 22, 21, 19]

# Creazione del line plot
plt.plot(ore, temperatura)

# Etichette per gli assi
plt.xlabel('Ore del giorno')
plt.ylabel('Temperatura (°C)')

# Titolo del grafico
plt.title('Andamento della temperatura durante la giornata')


# Cambiare colore e aggiungere punti sulla linea 
plt.plot(ore, temperatura, color='blue', marker='o')


# Visualizzazione del grafico
plt.show()
