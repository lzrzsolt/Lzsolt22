def szam (*float):
    try:

        print(a/b)
    except ZeroDivisionError:
        print("Division by zero not allowed")

    finally:
        print("Out of try except blocks")


if __name__ == "__main__":
    i = 1
    while i < 6:
        a=float(input("Enter 'a' value:"))
        b=float(input("Enter 'b' value:"))
        szam(a,b)
