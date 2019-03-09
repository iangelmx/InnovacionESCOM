#include <iostream>
#include <cstdlib>
using namespace std;


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
