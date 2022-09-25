def szöveg(name):
    szótár={}
    szám=0
    for karakter in mondat:
        for karakter2 in mondat:
            if karakter==karakter2:
                szám=szám+1
                szótár[karakter]=szám
        szám=0


    print("Betűk gyakorisága:", szótár)
    print("Fordítva:", mondat[::-1])
    rendezés=[mondat.split(" ")]
    print("Listába rendezve szavanként:", rendezés)




if __name__=="__main__":
    print("Adjon meg egy mondatot:")
    mondat=input()
    szöveg(mondat)