from datetime import datetime

class ContoCorrente:
    def __init__(self,cc,PW,IBAN,BIC,banca,s,c):
        self.__saldo=s
        self.__PW=PW
        self.__IBAN=IBAN
        self.__cod_conto=cc
        self.__BIC=BIC#possibiltà di implementazione di trasferimenti con il codice bic
        self.__banca=banca
        self.__circolo="Visa"
        self.__listTransaction=[]
        self.__clienti=c#per un eventuale doppio controllo


    def aggiungiClienteGestioneConto(self,c):
        self.__clienti.append(c)

    def controlloCre(self,cod_conto,PW):
        if(self.__PW==PW and self.__cod_conto==cod_conto):
            return True
        return False

    def possibilitàTrans(self,s):
        if (s<= self.__saldo):
            return True
        return False

    def getIBAN(self):
        return self.__IBAN

    def aggiornaSaldo(self,s):
        self.__saldo+=s
    '''
    def trans(self,IBAN_m,IBAN_d,s):
        desc = [datetime.now(),IBAN_m,IBAN_d]
        if(self.__IBAN==IBAN_m and self.possibilitàTrans(s)==True):
            self.aggiornaSaldo(-s)
            desc.append[-s]
        elif(self.__IBAN==IBAN_d):
            self.aggiornaSaldo(s)
            desc.append[-s]
        else:
            print(f"vi è un errore nell'inserimento degli IBAN o non si posssiedono abbastanza soldi sul conto, ritentare o cambiare operazione, grazie")
            return
        self.__listTransaction.append(desc)
    '''
    def sendMoney(self,IBAN_d,s):
        if(self.possibilitàTrans(s) == True):
            desc = [datetime.now(), self.__IBAN, IBAN_d,-s]
            self.__listTransaction.append(desc)
            self.aggiornaSaldo(-s)
            self.__banca.sendMoney(self.__IBAN, IBAN_d,s)

    def getMoney(self,IBAN_m,s):
        desc = [datetime.now(), IBAN_m , self.__IBAN, s]
        self.__listTransaction.append(desc)
        self.aggiornaSaldo(s)


    def showTrans(self):
        print(f"data e ora,\tIBAN_m,\tIBAN_d,\t denaro trasferito")
        for x in self.__listTransaction:
            print(f"{x[0]},\t{x[1]},\t{x[2]},\t{x[3]}")







