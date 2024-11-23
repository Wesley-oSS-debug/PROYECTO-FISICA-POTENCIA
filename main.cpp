#include <iostream>
#include "funciones.h"
#include <fstream>
using namespace std;

int main() {
	int op;
	string linea;
	ofstream archivo;
	ifstream archivo2;
	archivo.open("TFConst.txt",ios::app); //ios::app para seguir escribiendo
	do {
		int n=0;
		archivo2.open("TFConst.txt");
		while (getline(archivo2,linea)) {
			n++;
		}
	archivo2.close();
		system("cls");
		cout<<"---------MENU PRINCIPAL---------"<<endl
			<<"1. Calcular Trabajo de una fuerza constante"<<endl
			<<"2. Calcular Trabajo de una fuerza variable"<<endl
			<<"3. Calcular Trabajo consumido por un resorte"<<endl
			<<"4. Calcular Potencia"<<endl
			<<"5. Mostrar datos de trabajo de fuerza constante"<<endl
			<<"0. Salir del programa"<<endl
			<<"Ingrese una opcion: "; cin>>op;
		switch (op) {
			case 1:
				TrabajoFuerzaConst(archivo);
				break;
			case 2:
				break;
			case 3:
				break;
			case 4:
				break;
			case 5:
				archivo2.open("TFConst.txt");
				mostrarDatos(archivo2,n);
				archivo2.close();
				break;
		}
	} while (op!=0);
	archivo.close();
	return 0;
}