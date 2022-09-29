
class Cliente:
    def __init__(self,nome,cognome,ID,PW):
        self.__nome=nome
        self.__cognome=cognome
        self.__ID=ID
        self.__PW=PW
        self.__conti=dict()

    # dovrebbe rilasciare un certificato che cretifica l'avvenuto accesso alla sessione corrente e
    # controllare la validità di tale certificato prima di effettuare qualcunque altra operazione
    def accessoAPP(self,ID,PW):
        if (self.__PW==PW and self.__ID==ID):
           return True
        else:
            return False

    def accessoCC(self,cod_conto,PW):
        if len(self.__conti)==0:
            return False
        for x in self.__conti.keys():
            if x==cod_conto and self.__conti[x]==PW:
                return True
        return False


    def newCC(self,cc,pw):
        self.__conti[cc]=pw

