class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def getId(self) -> str:
        return self.__id
    def getNumber(self) -> str:
        return self.__number

    def isValid(self) -> bool:
        permitidos = "0123456789()."
        for numero in self.__number:
            if numero not in permitidos:
                return False
        return True 

    def __str__(self) -> str:
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name: str):
        self.__favorited : bool = False
        self.__fones : list[Fone] = []
        self.__name: str = name

    def getFones(self):
        return self.__fones
    def getName(self) -> str:
        return self.__name
    def setName(self, name: str):
        self.__name = name

    def addFone(self, id : str, number : str) -> None:
       fone = Fone(id, number)
       if not fone.isValid():
            raise Exception("fail: invalid number")
       self.__fones.append(fone)

    def rmFone(self, index: int) -> None:
        del self.__fones[index]

    def favoritar(self) -> bool:
        return self.__favorited

    def tooglefavourite(self) -> bool:
        self.__favorited = not self.__favorited

    def __str__(self) -> str:
        arroba = "@ " if self.__favorited else "- "
        lista = ", ".join(str(fone) for fone in self.__fones)
        return f"{arroba}{self.__name} [{lista}]"

    



def main():
    contact = Contact(" ")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        try:
            if args[0] == "end":
                break
            elif args[0] == "init":
                name = str(args[1])
                contact.setName(name)
            elif args[0] == "add":
                id = args[1]
                number = args[2]
                contact.addFone(id, number)
            elif args[0] == "show":
                print(contact)
            elif args[0] == "rm":
                index = int(args[1])
                contact.rmFone(index)
            elif args[0] == "tfav":
                contact.tooglefavourite()


            else:
                print("comando invalido")
        except Exception as e:
            print(e)
       
            
       
main()




