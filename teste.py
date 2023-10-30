class Bank:
    def __init__(self, clienti, tranzactii):
        self.clienti = clienti
        self.tranzactii = tranzactii

class Clienti:
    def __init__(self, UID, nume_prenume):
        self.UID = UID
        self.nume_prenume = nume_prenume

class Tranzactii:
    def __init__(self, TID, UID, suma, tip, zi):
        self.TID = TID
        self.UID = UID
        self.suma = suma
        self.tip = tip
        self.zi = zi