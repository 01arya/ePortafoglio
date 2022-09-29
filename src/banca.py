from abc import ABCMeta, abstractmethod
from cc import *
class Interface:
    @abstractmethod
    def sendMoney(self, IBAN_m, IBAN_d, s):
        pass


class Banca(Interface):
    def __init__(self, n, c):
        self.__cod_banca = c
        self.__nome = n
        self.__conti = list()
        self.__n_conti = 0
        self.__clienti=[]


    def addCli(self, c):
        self.__clienti.append(c)

    def delCli(self, c):
        self.__clienti.remove(c)

    def AddCC(self, c):
        self.__conti.append(c)
        self.__n_conti += 1

    def DelCC(self, c):
        self.__conti.remove(c)
        self.__n_conti -= 1

    def ret_N_CC(self):
        return self.__n_conti

    def sendMoney(self, IBAN_m, IBAN_d, s):
        #il mittente ha mandato soldi
        for x in self.__conti:
            if(x.getIBAN()==IBAN_d):#il destinatario è nella mia banca
                x.getMoney(IBAN_m,s)#aggiorno il saldo del destinatario

        #se non si trova nella lista non è nostro quindi non lo gestiamo

    def getCli(self):
        return self.__clienti



