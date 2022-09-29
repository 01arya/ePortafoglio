
from cliente import *
from cc import *
from banca import *
import string
import random

COD=111#codice identificativo del conto che incrementa ogni volta che si crea un conto
b=Banca("ePortafoglio",0)#la nostra banca

def creaConto(ID_cli):
    pw=input("inserire un pin/password di sicurezza per il conto: ")
    iban = ("IT" + ''.join(random.choice(string.digits) for i in range(2)) + ''.join(random.choice(string.ascii_uppercase) for i in range(23)))
    bic = ("EPORTFOLIO" + "RM" + "IT" + ''.join(random.choice(string.digits) for i in range(5)))
    iban= ('IT'+ '10010010'+ random.choice(string.ascii_letters) for i in range(10))
    s=input("inserire il saldo iniziale")
    c=ContoCorrente(COD,pw,iban,bic,"ePortfolio",s,ID_cli)
    COD+=1
    b.AddCC(c)


def accessoApp():
    ID = input("inserire il nome utente:")
    PW = input("inserire la password: ")
    b=False
    i=0
    for x in b.getCli[i]:
        i+=1
        if(x.accessoAPP==True):
            b=True
            break
    if (b==False):
        print(f"vi è stato un errore nell'inserimento dei dati di accesso, iserire nuovamente nome utente e password!")
        ID = input("inserire il nome utente:")
        PW = input("inserire la password: ")
        x.accessoApp(ID, PW)
    else:
        print("accesso effettuato correttamente! ")

        print("1- effettuare l'accesso a un conto corrente ")
        print("2- aprire un nuovo conto corrente ")
        print("3- uscire")
        s = input("")
        if (s == "1"):
            cod_conto = input("inserire il codice conto:")
            PW = input("inserire la password: ")
            b.getCli[i].accessoCC(cod_conto, PW)
        elif (s == "2"):
            creaConto(b.getCli[i])
        else:
            exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
