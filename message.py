class Message:
    def __init__(self, mittente, destinatario):
        self._mittente = mittente
        self._destinatario = destinatario
        self._corpoMessaggio = " "

    def append(self,riga):
        """Aggiunge una riga in fondo al testo del messaggio"""
        self._corpoMessaggio += riga + "\n"

    def toString(self):
        """Restituisce il testo del messaggio"""
        return "Mittente: " + self._mittente + "\nDestinatario: " + self._destinatario + "\n" +  self._corpoMessaggio

m = Message("io", "tu")
m.append("Ciao")
m.append("Come va?")
print(m.toString())
        