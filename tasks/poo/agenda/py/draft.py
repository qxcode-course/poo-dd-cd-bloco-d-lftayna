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

class Agenda:
    def __init__(self, contats: dict[Contact] = {} ):
        self.__contats: dict[Contact] = {}

    def addContact(self, name: str, fones: list[str]):
        if name not in self.__contats:
            self.__contats[name] = Contact(name)
        contact = self.__contats[name]

        for x in fones:
            if ":" not in x:
                raise Exception("fail: invalid format")
            id, number = x.split(":")
            contact.addFone(id, number)
    

    def __str__(self) -> str:
        contatosOrdenados = sorted(self.__contats.values(), key = lambda c: c.getName())
        return f"\n".join(str(c) for c in contatosOrdenados)
    
    def getContact(self, name : str) -> Contact | None:
        return self.__contats.get(name)
    
    def rm(self, name: str):
        if name in self.__contats:
                del self.__contats[name]
        else:
            print(f"fail:contato{name}nao existe")

    def search

def main():
    agenda = Agenda(" ")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            name = args[1]
            fones = args[2:]
            agenda.addContact(name, fones)
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)
            if contact is None:
                print(f"fail: contato {name} nao existe")
            else:
                contact.rmFone(index)
        elif args[0] == "rm":
            name = args[1]
            agenda.rm(name)
        ##elif args[0] == "search":
            
        
            
           
main() 

