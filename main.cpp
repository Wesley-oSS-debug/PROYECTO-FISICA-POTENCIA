#include <iostream>
#include "funciones.h"
using namespace std;

int main() {
	int op;
	
	do {
		system("cls");
		cout<<"---------MENU PRINCIPAL---------"<<endl
			<<"1. Calcular Trabajo de una fuerza constante"<<endl
			<<"2. Calcular Trabajo de una fuerza variable"<<endl
			<<"3. Calcular Trabajo consumido por un resorte"<<endl
			<<"4. Calcular Potencia"<<endl
			<<"0. Salir del programa"<<endl
			<<"Ingrese una opcion: "; cin>>op;
		switch (op) {
			case 1:
				TrabajoFuerzaConst();
				break;
			case 2:
				break;
			case 3:
				break;
			case 4:
				break;
		}
			
		
	} while (op!=0);
	return 0;
}