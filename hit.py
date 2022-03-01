
def calcMoy(note:float,coef:int):
    noteC=note*coef
    return noteC
def buildNote(filePath: str) -> str:
    with open(filePath,'r') as file:
        texte = file.read()
        return texte
        file.close()
        pass


def calc(note:float,coef:int):
    noteC=note*coef
    return noteC
def buildNote(filePath: str) -> str:
    with open(filePath,'r') as file:
        texte = file.read()
        return texte
        file.close()
        pass

def main() -> list:
    
    chaine = buildNote('C:/Users/user/Desktop/TP_PYTHON/files')
    ListeMots = []
    for index,value in enumerate(chaine):
        ListeMots.append(
             (value)
            )
        pass
    #ListeMots = sorted(ListeMots,reverse =True, key = lambda X: X[1])
    print(ListeMots)
    pass


if __name__ == '__main__':
    print(main())

