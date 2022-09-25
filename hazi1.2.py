def valtas(name, float):
    inch=2.54
    if mértékegység=="cm":
        print(szám/inch,"inches")
    elif mértékegység =="inch":
        print(szám*inch, "cms")


if __name__=="__main__":
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    szám=float(input())
    mértékegység=input()
    valtas(mértékegység,szám)


