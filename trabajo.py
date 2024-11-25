from tkinter import *
from tkinter import messagebox
import math

#CONFIGURACIONES VENTANA PRINCIPAL
raiz=Tk()
raiz.iconbitmap("work.ico")
raiz.title("TRABAJO")
raiz.geometry("800x800+500+100")
raiz.resizable("False","False")
raiz.config(bg="#ffecbd")
mainImage=PhotoImage(file="trabajo.png")
imgLbl=Label(raiz,image=mainImage)
imgLbl.grid(row=0,column=0,padx=150,pady=10)

def salir():
    valor=messagebox.askokcancel("Salir","Estas seguro que deseas salir?")
    if valor==True:
        raiz.destroy()

#VENTANA DE LA OPCION TRABAJO CONSTANTE
def trabajoC():
    vTF=Tk()
    vTF.title("Fuerza constante")
    vTF.geometry("300x200+750+400")
    
    fuerza=[]
    angulo=[]
    distancia=[]
    trabajo=[]
    datos=[fuerza,angulo,distancia,trabajo]
    
    #FUNCION QUE CALCULA EL TRABAJO DE UNA FUERZA CONSTANTE
    def calculo():
        try:
            f=float(fuerzaIn.get())
            a=float(anguloIn.get())
            d=float(distanciaIn.get())

            #VALIDACION DE DISTANCIA
            if d < 0:
                messagebox.showerror("Error", "La distancia no puede ser negativa")
                return

            aRad=math.radians(float(a))
            r=round(float(f)*float(d)*math.cos(aRad),2) #round(numero,decimales)
            
            datos[0].append(f)
            datos[1].append(a)
            datos[2].append(d)
            datos[3].append(r)
            
            resultadoIn.config(state="normal")
            resultadoIn.delete(0,"end")
            resultadoIn.insert(0,r)
            resultadoIn.config(state="readonly")
        
        except ValueError:

            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
        
    def mostrarDatos():
        vDat=Tk()
        vDat.title("Datos")
        vDat.geometry("550x400+100+300")
        
        #Labels
        fLbl=Label(vDat, text="Fuerza", bg="yellow", width=14, height=1)
        fLbl.grid(row=0,column=0, padx=10, pady=5)
        
        aLbl=Label(vDat, text="Angulo",bg="yellow", width=14, height=1)
        aLbl.grid(row=0,column=1, padx=10, pady=5)
        
        dLbl=Label(vDat, text="Distancia",bg="yellow", width=14, height=1)
        dLbl.grid(row=0,column=2, padx=10,pady=5)
        
        tLbl=Label(vDat,text="Trabajo",bg="yellow", width=14, height=1)
        tLbl.grid(row=0,column=3, padx=10, pady=5)
        
        #Entrys
        
        for i in range(len(datos[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(vDat, justify="center")
            fIn.grid(row=i+1,column=0,padx=10)
            fIn.insert(0,datos[0][i])
            fIn.config(state="readonly")

            aIn=Entry(vDat,justify="center")
            aIn.grid(row=i+1,column=1)
            aIn.insert(0,datos[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(vDat,justify="center")
            dIn.grid(row=i+1,column=2, padx=10)
            dIn.insert(0,datos[2][i])
            dIn.config(state="readonly")
            
            tIn=Entry(vDat,justify="center")
            tIn.grid(row=i+1,column=3)
            tIn.insert(0,datos[3][i])
            tIn.config(state="readonly")

    #LABEL,ENTRY Y BOTONES
    fuerzaLbl=Label(vTF, text="Fuerza:")
    fuerzaLbl.grid(row=0,column=0, sticky="e", padx=10, pady=5)
    
    fuerzaIn=Entry(vTF, justify="center")
    fuerzaIn.grid(row=0,column=1)
    
    anguloLbl=Label(vTF, text="Angulo:")
    anguloLbl.grid(row=1,column=0, sticky="e", padx=10, pady=5)
    
    anguloIn=Entry(vTF,justify="center")
    anguloIn.grid(row=1,column=1)
    
    distanciaLbl=Label(vTF, text="Distancia:")
    distanciaLbl.grid(row=2,column=0, sticky="e", padx=10,pady=5)
    
    distanciaIn=Entry(vTF,justify="center")
    distanciaIn.grid(row=2,column=1)
    
    btn=Button(vTF, text="Calcular", command=calculo)
    btn.grid(row=1,column=2, padx=10)
    
    resultadoLbl=Label(vTF,text="Resultado:")
    resultadoLbl.grid(row=3,column=0, padx=10, pady=5)
    
    resultadoIn=Entry(vTF, readonlybackground="yellow",state="readonly",justify="center")
    resultadoIn.grid(row=3,column=1)
    
    mostrarBtn=Button(vTF, text="Mostrar Datos", command=mostrarDatos)
    mostrarBtn.grid(row=4,column=1, pady=30)

#BOTONES
btn1=Button(raiz, text="Teoria de TRABAJO")
btn1.grid(row=1,column=0,pady=10)

btn2=Button(raiz, text="Calcular Trabajo de una fuerza constante", command=trabajoC)
btn2.grid(row=2,column=0,pady=10)

btn3=Button(raiz, text="Calcular Trabajo de una fuerza variable")
btn3.grid(row=3,column=0,pady=10)

btn0=Button(raiz, text="Salir del programa", fg="red", command=salir)
btn0.grid(row=4,column=0,pady=10)

raiz.mainloop()