class team:
    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print("-- Developer létrehozva. --")
        print(self)



    def __str__(self):
        return self._nev + " a " + str(self._projekt)+"en dolgozik " + str(self._szerepkor)+" szerepkörben"


def osszehasonlitas (*team):
    lista=[x1, x2, x3, x4]

    for elem in lista:
        for elem2 in lista:
            if elem._projekt == elem2._projekt and elem._nev != elem2._nev:
                 print(elem._nev + " és " + elem2._nev + " dolgoznak egy projekten. ")
                 lista.remove(elem)

if __name__== '__main__':
    x1 = team("Ricsi", "SolArch", "Frontend")
    x2 = team("Angéla", "ZerTeng", "Tesztelő")
    x3 = team("Peti", "KefERP", "Backend")
    x4 = team("Éva", "KefERP", "Frontend")
    osszehasonlitas(x1, x2 ,x3, x4)


