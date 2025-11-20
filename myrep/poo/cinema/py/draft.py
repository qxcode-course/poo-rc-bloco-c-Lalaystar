class Client:
    def __init__(self, id:str, phone:int):
        self.__id=id
        self.__phone=phone

    def getId(self)->str:
        return self.__id
    
    def getPhone(self)->int:
        return self.__phone
    
    def setId(self, id:str):
        self.__id=id

    def setPhone(self, phone:int):
        self.__phone=phone 

class Theater:
    