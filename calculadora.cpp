
#include <iostream>
#include <cstdlib>
using namespace std;

void restar (float a, float b){
     c=a-b;
    cout << "Resultado: " << c; 
 }


void potenciacion(int a, int b){
  int a;
  int b;
    cout<<"Ingrese los valores para calcular la potencia"<<endl;
    cout<<"Ingrese el valor a potenciar"<<endl;
    cin>>a;
    cout<<"Ingrese el valor de la potencia"<<endl;
    cin>>b;
    c=exp(a,b);
    cout<<"El resultado de la exponencial es:"<<c;
}

void sumar (float a, float b)
{
    float c;
    cin >> a;
    cin >> b;
    c=a+b;
    cout << "Resultado: " << c; 
 }

float Dividir (float,float);

int main()
{
	system ("1c");
	float a,b,c;
	cout<<"La Calculadora"<<endl;
	cout<<endl<<"Dividir: "<<endl<<endl;
	cout<<"Ingrese Dividendo: ";
	cin>>a;
	cout<<"Ingrese Divisor: ";
	cin>>b;
	c=Dividir(a,b);
	cout<<endl<<endl<<"Resultado: "<<c<<endl;
	
	return 0;
}

float Dividir (float a, float b)
{
	float c;
	c=a/b;
	return c;
}
