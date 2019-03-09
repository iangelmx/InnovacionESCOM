#include <iostream.h>
#include <stdio.h>
#include <stlib.h>
using namespace std;

int a;
int b;

void main{
    cout<<"Ingrese los valores para calcular la potencia"<<endl;
    cout<<"Ingrese el valor a potenciar"<<endl;
    cin>>a;
    cout<<"Ingrese el valor de la potencia"<<endl;
    cin>>b;
    c=exp(a,b);
    cout<<"El resultado de la exponencial es:"<<c;
    return 0;
}