import webbrowser  

def opcion1():
    # El enlace de Google Docs que quieres abrir
    url = "https://docs.google.com/document/d/1kW4qjYgFTEPtui10ZwKWFCUTTVd68vTgg5oGKePvCjY/edit?hl=es&tab=t.0"
    
    try:
        webbrowser.open(url, new=2)  # 'new=2' intenta abrir la URL en una nueva ventana del navegador
        print(f"\nSe está abriendo la teoria...\n")
    except Exception as e:
        print(f"\nOcurrió un error al intentar abrir la URL\n")

def opcion2():
    print("\nAqui se calcula el trabajo...\n")

def opcion3():
    print("\nAqui se calcula el trabajo consumido por un resorte...\n")

def opcionSalir():
    print("Saliendo del programa...")
    return True  

def opcionInvalida():
    print("Opcion invalida.\n")
    return False  

# Diccionario que es parecido al switch
switch = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    0: opcionSalir  
}

def evaluarOpcion(opcion):
    return switch.get(opcion, opcionInvalida)()  

while True:
    try:
        print(f"TRABAJO\n"
              f"1. Teoria\n"
              f"2. Calculo de Trabajo\n"
              f"3. Trabajo consumido por un resorte\n"
              f"0. Salir\n")
        opcion = int(input("Digite una opción: "))

        if evaluarOpcion(opcion):  
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")
