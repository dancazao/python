

class User:
    codigo=1

    def __init__(self,login:str,senha:str,saldo:int=0):
        self.__login=login
        self.__senha=senha
        self.__saldo=saldo
        #User.codigo+=1

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,novo_saldo):
        self.__saldo=novo_saldo




class Admim:
    def __init__(self):
        pass
