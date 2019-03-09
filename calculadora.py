
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
      
#This function subtract two numbers
def sub(a,b):
    return a-b
