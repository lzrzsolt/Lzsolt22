def haromszog ( * int ) :
    kiirando = "A {}, {} és {} oldalú háromszög"
    if a+b>c and a+c>b and b+c>a:
        print(kiirando.format(a,b,c), "szerkeszthető")
    else:
        print(kiirando.format(a,b,c), "nem szerkeszthető")
if __name__=="__main__":
    print("Adja meg a háromszög három oldalát cm-ben:")
    a=input("a oldal (cm)")
    b=input("b oldal (cm)")
    c=input("c oldal (cm)")
    haromszog(a,b,c)
