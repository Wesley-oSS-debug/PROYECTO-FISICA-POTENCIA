#include <iostream>
#include <cmath>
#include "funciones.h"
#include <fstream>

using namespace std;

void TrabajoFuerzaConst(ofstream &archivo) {
	
	float fuerza,distancia,angulo,trabajo;
	system("cls");
	cout<<"CALCULO DEL TRABAJO INVERTIDO POR UNA FUERZA CONSTANTE"<<endl
		<<"Ingrese la fuerza constante (N): "; cin>>fuerza;
	cout<<"Ingrese el angulo de inclinacion de la fuerza: "; cin>>angulo;
	cout<<"Ingrese la distancia recorrida (m): "; cin>>distancia;
	angulo=angulo*M_PI/180;
	trabajo=fuerza*cos(angulo)*distancia;
	cout<<"El trabajo consumido por la fuerza es de "<<trabajo<<" Joules"<<endl;
	archivo<<fuerza<<" "<<angulo<<" "<<distancia<<" "<<trabajo<<endl;
	system("pause");
	
}