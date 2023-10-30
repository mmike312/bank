from random import randint

#clasele de obiecte
class Bank:
    def __init__(self, clienti, tranzactii):
        self.clienti = []
        self.tranzactii = []

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

#interfata
def meniu():
    print("1 - Aduga tranactie")
    print("2 - Sterge tranzactie")
    print("3 - Cautare")
    print("4 - Genereaza raport")
    print("5 - Filtreaza")
    print("6 - Undo")

def meniu1():
    print("1 - Adauga o tranzactie noua")
    print("2 - Actualizeaza o treanzactie existenta")

def meniu2():
    print("1 - Sterge toate tranzactiile din data zi:luna:an")
    print("2 - Sterge toate tranzactiile din perioada z1:l1:a1 - z2:l2:a2")
    print("3 - Sterge tranzactiile de")

def meniu3():
    print("1 - Afiseaza tranzactiile cu sume mai mari de o suma x")
    print("2 - Soldul la data zz:luna:an")

def meniu4():
    print("1 - Suma totala a tranzactiilor de tipul y")
    print("2 - Soldul unui cont la data zi:luna:an")
    print("3 - Toate tranzactiile de tipul y in ordine descrescatoare a sumei")

def meniu5():
    print("Aplica filtru:")
    print("1 - Elimina tranzactiile de tipul y")
    print("2 - Elimina tranzactiile mai mari de x lei")

def meniu6():
    print("1 - Sterge ultima tranzactie")
    print("2 - Sterge urmatoarele tranzactii dupa ID")

def logoBanca(): 
    print("       .  .  .   . .      .            ..    .       .  .")
    print(" ..          .        .  .               .     .        .")
    print(".  .     .   .          ....:...     . . .    . .       .")
    print("     .                ..-**+=+**-..      .        .      ")
    print(" .   ..    .      ..:+*+=::::::-=+*+:..                  ")
    print("         ...:::::+*+=-::==---=---::-=+*+::::::.        ..")
    print("      .....-=+*+=-:::::::::::::::::::::-=+*+=-.....  ....")
    print("      .-+++++++++++++++++++++++++++++++++++++++++=.      ")
    print("     ....----=------=---------------=------=----..       ")
    print(" .      .:-------------------------------------:.        ")
    print("     .  ..::====:::=++=.::+++++::.=+++:::=++=::..  .... .")
    print(".   . . ..:-=**=::=+*#+-:=+##*+=:-+##*=:-+##*=:..  .    .")
    print("        ..:-=++=::=+++=-:=+***+=:-+***=:-***+-:..      . ")
    print(".       ..:--:::::=-::-::=+===+=:-=====:-====-:..       .")
    print("  .  .  ..:-=---::=----::-=*#*+=::++++=:-++++-:..    .   ")
    print("    .   ..:-=**=::-+*#=:::+#%%*=::+##*=::+##*-:..   .    ")
    print("       ...:-=++=::-+++=:::++#**-::+***-::***+-:..   .  . ")
    print(".       .:::=---:::----:::+#%#*-::===+-::====:::..   .   ")
    print(" .      .+***************++%%%++***************+..  .    ")
    print("#########################################################")
    print()
    print(" ____    _    _   _  ____    _      _    _   _ ___ ")
    print("| __ )  / \  | \ | |/ ___|  / \    | |  | | | |_ _|")
    print("|  _ \ / _ \ |  \| | |     / _ \   | |  | | | || | ")
    print("| |_) / ___ \| |\  | |___ / ___ \  | |__| |_| || | ")
    print("|____/_/___\_\_|_\_|\____/_/_  \_\ |_____\___/|___|")
    print("           |  \/  |_ _| | | |  / \  |_ _|")                     
    print("           | |\/| || || |_| | / _ \  | | ")                   
    print("           | |  | || ||  _  |/ ___ \ | | ")                     
    print("           |_|  |_|___|_| |_/_/   \_\___|")          
    print()
    print("#########################################################")     

#navigare meniuri

def navigareMeniuPrincipal(o):
    ok = False
    while ok == False:
        meniu()
        x = inputInt( int(1), int(6), "Alege o optiune: ")
        if x == 1:
            navigareMeniuAdaugare(o)
        elif x == 2:
            pass
        elif x == 3:
            pass
        elif x == 4:
            pass
        elif x == 5:
            pass
        elif x == 6:
            ok = True

def navigareMeniuAdaugare(o):
    ok = False
    while ok == False:
        x = inputInt( int(1), int(4), "Ce ai vrea sa adaugi? ")
        if x == 1:
            adaugaUser(o)
        elif x == 2:
            pass
        elif x == 3:
            pass
        elif x == 4:
            ok = True
    

#aplicatia - main -

def app():
    o = Bank( [], [])
    logoBanca()
    navigareMeniuPrincipal(o)
    
    

#input
def inputInt( i = None, s = None, mesaj = ""):
    """
        Cere input pana cand se itroduce o valoare valida, numar intreg
        La apelarea fara parametri:

        inputInt()

        La aperlarea cu parametri:
        
        inputInt( limita inferioara a numarului valid, limita superioara a numarului valid), mesajul afisat la input)
    """
    ok = False
    x = None
    while ok == False:
        x = input(mesaj)
        try:
            x = int( x)
        except:
            print("Introdu un numar natural care sa corespunda unei optiuni din meniu!!!")
        c = int( 9)
        if type(x) == type(c):
            if i != None and  s!= None:
                if i > x or x > s:
                    print("Introdu un numar cuprins intre", i, "si", s, "!!!")
                else:
                    ok = True
            else:
                return True
       
    return int(x)                
        
#adaugari

def adaugaUser(o):
    x = genereazaID(o.clienti)
    np = input("Nume si prenume client nou: ")
    cl = Clienti(x, np)
    o.clienti.append(cl)
    print( o.clienti[0].UID, o.clienti[0].nume_prenume)

#diverse

def genereazaID(l_clienti):
    ok = False
    while ok == False:
        x = randint(1000, 9999)
        ok = True
        for i in l_clienti:
            if i.UID == x:
                ok = False
    return x


#teste

def testInputInt():
    assert type(inputInt()) == 'int'
    assert (inputInt( 1, 6) <= 6) or (inputInt(1,6) >= 1)


app()





