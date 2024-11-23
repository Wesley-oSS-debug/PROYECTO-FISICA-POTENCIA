#include <iostream>
#include <fstream>
#include "funciones.h"
using namespace std;

void mostrarDatos(ifstream &archivo2,int n) {
	float fuerza,distancia,angulo,trabajo;
	for (int i=0;i<n;i++) {
		archivo2>>fuerza>>angulo>>distancia>>trabajo;
		cout<<"Fuerza: "<<fuerza<<endl;
		cout<<"Angulo: "<<angulo<<endl;
		cout<<"Distancia: "<<distancia<<endl;
		cout<<"Trabajo: "<<trabajo<<endl;
		cout<<"-----------------------------"<<endl;
	}
	system("pause");
}