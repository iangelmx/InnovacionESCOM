def product(a,b):
    return (a*b)

def menu():
    print("\n\tCALCULATOR\n")
    print("1. Addition.")
    print("2. Subtraction.")
    print("3. Product")
    print("4. Quotient")
    print("5. Pow")
    a=input("Enter first number:")
    b=input("Enter second number:)
    option = input("Choose an option: ")
    if option=='1':
        r=sumar(a,b)
    elif option=='2':
        r=sub(a,b)
    elif option=="3":
        r=product(a,b)
    elif option=="4":
        r=dividir(a,b)
    elif option=="5":
        r=potencia(a,b)
    else:
        print("INEXISTENT OPTION")
    print("The result is: "+r)

if __name__ == '__main__':
    while True:
        menu()