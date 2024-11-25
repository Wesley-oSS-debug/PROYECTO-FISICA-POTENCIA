from tkinter import *
from tkinter import messagebox
import math

#ARREGLOS

#arreglos de trabajo fuerza constante
fuerza=[]
angulo=[]
distancia=[]
trabajo=[]
datosTFC=[fuerza,angulo,distancia,trabajo]

#CONFIGURACIONES VENTANA PRINCIPAL
raiz=Tk()
raiz.iconbitmap("work.ico")
raiz.title("TRABAJO")
raiz.geometry("800x800+500+100")
raiz.resizable("False","False")
raiz.config(bg="#ffecbd")
mainImage=PhotoImage(file="trabajo.png")
#frame de la imagen
frameImg=Frame(raiz,bg="#ffecbd")
frameImg.grid(row=0,column=0,pady=30)
imgLbl=Label(frameImg,image=mainImage)
imgLbl.grid(row=0,column=0,padx=140)

def salir():
    valor=messagebox.askokcancel("Salir","Estas seguro que deseas salir?")
    if valor==True:
        raiz.destroy()

#VENTANA DE LA OPCION TRABAJO CONSTANTE
def trabajoC():
    vTF=Tk()
    vTF.title("Fuerza constante")
    vTF.geometry("300x200+750+400")
    
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
            r=round(float(f)*float(d)*math.cos(aRad),4) #round(numero,decimales)
            
            datosTFC[0].append(f)
            datosTFC[1].append(a)
            datosTFC[2].append(d)
            datosTFC[3].append(r)
            
            resultadoIn.config(state="normal")
            resultadoIn.delete(0,"end")
            resultadoIn.insert(0,r)
            resultadoIn.config(state="readonly")

        except ValueError:
            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
        
    def mostrarDatos():
        if len(datosTFC[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vTF.destroy()
            return;
        vDat=Tk()
        vDat.title("Datos")
        vDat.geometry("550x400+100+300")
        vDat.resizable(0,0)
        frameLista=Frame(vDat)
        frameLista.grid(padx=2)
        #Labels
        fLbl=Label(frameLista, text="Fuerza", bg="yellow", width=14, height=1)
        fLbl.grid(row=0,column=0, padx=10, pady=5)
        
        aLbl=Label(frameLista, text="Angulo",bg="yellow", width=14, height=1)
        aLbl.grid(row=0,column=1, padx=10, pady=5)
        
        dLbl=Label(frameLista, text="Distancia",bg="yellow", width=14, height=1)
        dLbl.grid(row=0,column=2, padx=10,pady=5)
        
        tLbl=Label(frameLista,text="Trabajo",bg="yellow", width=14, height=1)
        tLbl.grid(row=0,column=3, padx=10, pady=5)
        
        #Entrys
        
        for i in range(len(datosTFC[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+1,column=0,padx=10)
            fIn.insert(0,datosTFC[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+1,column=1)
            aIn.insert(0,datosTFC[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+1,column=2, padx=10)
            dIn.insert(0,datosTFC[2][i])
            dIn.config(state="readonly")
            
            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+1,column=3)
            tIn.insert(0,datosTFC[3][i])
            tIn.config(state="readonly")



    
    #LABEL,ENTRY Y BOTONES
    frameEnt=Frame(vTF)
    frameEnt.grid(padx=10,pady=15)
    
    fuerzaLbl=Label(frameEnt, text="Fuerza:")
    fuerzaLbl.grid(row=0,column=0, sticky="nsew", padx=10, pady=5)
    
    fuerzaIn=Entry(frameEnt, justify="center")
    fuerzaIn.grid(row=0,column=1)
    
    anguloLbl=Label(frameEnt, text="Angulo:")
    anguloLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    anguloIn=Entry(frameEnt,justify="center")
    anguloIn.grid(row=1,column=1)
    
    distanciaLbl=Label(frameEnt, text="Distancia:")
    distanciaLbl.grid(row=2,column=0, sticky="nsew", padx=10,pady=5)
    
    distanciaIn=Entry(frameEnt,justify="center")
    distanciaIn.grid(row=2,column=1)
    
    btn=Button(frameEnt, text="Calcular", command=calculo)
    btn.grid(row=1,column=2, padx=10)
    
    resultadoLbl=Label(frameEnt,text="Resultado:")
    resultadoLbl.grid(row=3,column=0,sticky="nsew", padx=10, pady=5)
    
    resultadoIn=Entry(frameEnt, readonlybackground="yellow",state="readonly",justify="center")
    resultadoIn.grid(row=3,column=1)
    
    mostrarBtn=Button(frameEnt, text="Mostrar Datos", command=mostrarDatos)
    mostrarBtn.grid(row=4,column=1, pady=20)

def potencia():
    vTF=Tk()
    vTF.title("Potencia")
    vTF.geometry("300x200+750+400")

    trabajoPotencia=[]
    tiempo=[]
    potencia=[]
    datosPotencia=[trabajoPotencia, tiempo, potencia]

    #FUNCION PARA CALCULAR POTENCIA
    def calculoPotencia():
        try:

            w=float(trabajoPotenciaIn.get())
            t=float(tiempoIn.get())

            if t < 0:
                messagebox.showerror("Error", "El tiempo no puede ser negativo")
                return

            p=round(float(w)/float(t),4)

            datosPotencia[0].append(w)
            datosPotencia[1].append(t)
            datosPotencia[2].append(p)

            resultadoPotenciaIn.config(state="normal")
            resultadoPotenciaIn.delete(0,"end")
            resultadoPotenciaIn.insert(0,p)
            resultadoPotenciaIn.config(state="readonly")
        
        except ValueError:
            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
    
    def mostrarDatosPotencia():
        vDat=Tk()
        vDat.title("Datos")
        vDat.geometry("550x400+100+300")
        
        #Labels
        fLbl=Label(vDat, text="Trabajo", bg="yellow", width=14, height=1)
        fLbl.grid(row=0,column=0, padx=10, pady=5)
        
        aLbl=Label(vDat, text="Tiempo",bg="yellow", width=14, height=1)
        aLbl.grid(row=0,column=1, padx=10, pady=5)
        
        dLbl=Label(vDat, text="Potencia",bg="yellow", width=14, height=1)
        dLbl.grid(row=0,column=2, padx=10,pady=5)
        
        #Entrys
        
        for i in range(len(datosPotencia[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(vDat, justify="center")
            fIn.grid(row=i+1,column=0,padx=10)
            fIn.insert(0,datosPotencia[0][i])
            fIn.config(state="readonly")

            aIn=Entry(vDat,justify="center")
            aIn.grid(row=i+1,column=1)
            aIn.insert(0,datosPotencia[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(vDat,justify="center")
            dIn.grid(row=i+1,column=2, padx=10)
            dIn.insert(0,datosPotencia[2][i])
            dIn.config(state="readonly")

    #LABEL,ENTRY Y BOTONES
    trabajoPotenciaLbl=Label(vTF, text="Trabajo:")
    trabajoPotenciaLbl.grid(row=0,column=0, sticky="e", padx=10, pady=5)
    
    trabajoPotenciaIn=Entry(vTF, justify="center")
    trabajoPotenciaIn.grid(row=0,column=1)
    
    tiempoLbl=Label(vTF, text="Tiempo:")
    tiempoLbl.grid(row=1,column=0, sticky="e", padx=10, pady=5)
    
    tiempoIn=Entry(vTF,justify="center")
    tiempoIn.grid(row=1,column=1)
    
    btn=Button(vTF, text="Calcular", command=calculoPotencia)
    btn.grid(row=1,column=2, padx=10)
    
    resultadoPotenciaLbl=Label(vTF,text="Resultado:")
    resultadoPotenciaLbl.grid(row=2,column=0, padx=10, pady=5)
    
    resultadoPotenciaIn=Entry(vTF, readonlybackground="yellow",state="readonly",justify="center")
    resultadoPotenciaIn.grid(row=2,column=1)
    
    mostrarBtn=Button(vTF, text="Mostrar Datos", command=mostrarDatosPotencia)
    mostrarBtn.grid(row=3,column=1, pady=30)

#BOTONES MENU PRINCIPAL
#frame de botones
frameBtn=Frame(raiz, bg="#ffecbd")
frameBtn.grid()
btn1=Button(frameBtn, text="Teoria de TRABAJO")
btn1.grid(row=1,column=0,pady=10)

btn2=Button(frameBtn, text="Calcular Trabajo de una fuerza constante", command=trabajoC)
btn2.grid(row=2,column=0,pady=10)

btn3=Button(frameBtn, text="Calcular Trabajo de una fuerza variable")
btn3.grid(row=3,column=0,pady=10)

btn4=Button(frameBtn, text="Calcular Potencia", command=potencia)
btn4.grid(row=4,column=0,pady=10)

btn0=Button(frameBtn, text="Salir del programa", fg="red", command=salir)
btn0.grid(row=5,column=0,pady=10)

raiz.mainloop()