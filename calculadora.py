

"""
funcion que eleve a la potencia 2 2 numeros
"""
import numpy as np
def potencia(num1,num2):
    operacion = num1**num2
    return operacion
  
# función que suma dos números
def sumar(a, b):
    return a + b

#this function divide a by b
def dividir(a, b):
    if b == 0:
        print('You can not divide by 0')
        return 'Error'
    else:
        return a/b
def product(a,b):
 """This function multiply two numbres : a and b"""
  return (a*b)
#This function subtract two numbers
def sub(a,b):
    return a-b

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