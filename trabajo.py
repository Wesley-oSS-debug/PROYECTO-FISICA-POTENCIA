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
#arreglos de potencia
trabajoPotencia=[]
tiempo=[]
potencia=[]
datosPot=[trabajoPotencia, tiempo, potencia]

#CONFIGURACIONES VENTANA PRINCIPAL
raiz=Tk()
raiz.iconbitmap("work.ico")
raiz.title("TRABAJO")
raiz.geometry("400x600+750+200")
raiz.resizable("False","False")
raiz.config(bg="#350b4b")
mainImage=PhotoImage(file="work.png")

titulo= Label(raiz, text ="CALCULO DEL TRABAJO", bg = "#F4D03F", fg = "#ffffff", font=("Impact", 20, "bold"))
titulo.grid(row=1,column=0,pady=10)
#frame de la imagen
frameImg=Frame(raiz,bg="#350b4b")
frameImg.grid(row=0,column=0,pady=12)
imgLbl=Label(frameImg,image=mainImage)
imgLbl.grid(row=0,column=0,padx=73)

def salir():
    valor=messagebox.askokcancel("Salir","Estas seguro que deseas salir?")
    if valor==True:
        raiz.destroy()

#VENTANA DE TEORIA DE TRABAJO
def teoriaTrabajo():
    teoria = Tk()
    teoria.title("Teoria")
    teoria.iconbitmap("work.ico")
    teoria.geometry("280x300+670+200")
    teoria.resizable(0,0)
    teoria.config(bg = "#350b4b")
    frameBtn=Frame(teoria, bg="#350b4b")
    frameBtn.grid()
    
    tituloTeoria = Label(frameBtn, text ="BIENVENIDO A TEORIA", bg = "#F4D03F", fg = "#ffffff", font=("Impact", 20, "bold"))
    tituloTeoria.grid(row=0,column=0,pady=25,padx=15)
    btn1=Button(frameBtn, text="Ver teoria en linea" ,bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"))
    btn1.grid(row=1,column=0,pady=10)
    btn1=Button(frameBtn, text="Descargar teoria",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"))
    btn1.grid(row=2,column=0,pady=10)
    btn1=Button(frameBtn, text="Ver teoria de forma local",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"))
    btn1.grid(row=3,column=0,pady=10)
    btn1=Button(frameBtn, text="Ver libros",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"))
    btn1.grid(row=4,column=0,pady=10)

#VENTANA DE LA OPCION TRABAJO CONSTANTE
def trabajoC():
    vTF=Tk()
    vTF.iconbitmap("work.ico")
    vTF.title("Fuerza constante")
    vTF.geometry("330x300+750+400")     
    vTF.config( bg= "#F4D03F")
    vTF.resizable(0,0)
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
        vDat.geometry("590x400+100+300")
        vDat.resizable(0,0)
        vDat.config( bg= "#F4D03F")
        frameLista=Frame(vDat, bg= "#F4D03F")
        frameLista.grid(padx=2)
        #Labels
        tituloHistorial = Label(frameLista, text="HISTORIAL DE TRABAJO", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
        tituloHistorial.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")


        fLbl=Label(frameLista, text="Fuerza", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        fLbl.grid(row=1,column=0, padx=10, pady=5)
        
        aLbl=Label(frameLista, text="Angulo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        aLbl.grid(row=1,column=1, padx=10, pady=5)
        
        dLbl=Label(frameLista, text="Distancia",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        dLbl.grid(row=1,column=2, padx=10,pady=5)
        
        tLbl=Label(frameLista,text="Trabajo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        tLbl.grid(row=1,column=3, padx=10, pady=5)
        
        #Entrys
        
        for i in range(len(datosTFC[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosTFC[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosTFC[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosTFC[2][i])
            dIn.config(state="readonly")
            
            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+2,column=3)
            tIn.insert(0,datosTFC[3][i])
            tIn.config(state="readonly")



    
    #LABEL,ENTRY Y BOTONES
    frameEnt=Frame(vTF, bg= "#F4D03F")
    frameEnt.grid(padx=10,pady=5)
    
    tituloHistorial = Label(frameEnt, text="TRABAJO DE UNA \nFUERTA CONSTANTE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorial.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    fuerzaLbl=Label(frameEnt, text="Fuerza:",bg= "#F4D03F" ,fg = "#ffffff", font=("Arial",11,"bold"))
    fuerzaLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    fuerzaIn=Entry(frameEnt, justify="center")
    fuerzaIn.grid(row=1,column=1)
    
    anguloLbl=Label(frameEnt, text="Angulo:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    anguloLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    anguloIn=Entry(frameEnt,justify="center")
    anguloIn.grid(row=2,column=1)
    
    distanciaLbl=Label(frameEnt, text="Distancia:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    distanciaLbl.grid(row=3,column=0, sticky="nsew", padx=10,pady=5)
    
    distanciaIn=Entry(frameEnt,justify="center")
    distanciaIn.grid(row=3,column=1)
    
    btn=Button(frameEnt, text="Calcular", command=calculo)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoLbl=Label(frameEnt,text="Resultado:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    resultadoLbl.grid(row=4,column=0,sticky="nsew", padx=10, pady=5)
    
    resultadoIn=Entry(frameEnt, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoIn.grid(row=4,column=1)
    
    mostrarBtn=Button(frameEnt, text="Mostrar Datos", command=mostrarDatos)
    mostrarBtn.grid(row=5,column=1, pady=20)

#VENTANA DE LA OPCION POTENCIA
def potencia():
    vP=Tk()
    vP.iconbitmap("work.ico")
    vP.title("Potencia")
    vP.geometry("310x200+750+400")
    vP.resizable(0,0)
    vP.config(bg="#F4D03F")

    #FUNCION PARA CALCULAR POTENCIA
    def calculoPotencia():
        try:

            w=float(trabajoPotenciaIn.get())
            t=float(tiempoIn.get())
            if t < 0:
                messagebox.showerror("Error", "El tiempo no puede ser negativo")
                return
            p=round(float(w)/float(t),2)
            datosPot[0].append(w)
            datosPot[1].append(t)
            datosPot[2].append(p)

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
        vDat.geometry("440x400+100+300")
        vDat.config(bg= "#F4D03F")
        vDat.resizable(0,0)
        #Labels
        tituloHistorialPotencia = Label(vDat, text="HISTORIAL DE POTENCIA", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
        tituloHistorialPotencia.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

        fLbl=Label(vDat, text="Trabajo", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        fLbl.grid(row=1,column=0, padx=10, pady=5)
        
        aLbl=Label(vDat, text="Tiempo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        aLbl.grid(row=1,column=1, padx=10, pady=5)
        
        dLbl=Label(vDat, text="Potencia",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        dLbl.grid(row=1,column=2, padx=10,pady=5)
        
        #Entrys
        
        for i in range(len(datosPot[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(vDat, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosPot[0][i])
            fIn.config(state="readonly")

            aIn=Entry(vDat,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosPot[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(vDat,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosPot[2][i])
            dIn.config(state="readonly")

    #LABEL,ENTRY Y BOTONES

    tituloPotencia = Label(vP, text="  POTENCIA", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloPotencia.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    trabajoPotenciaLbl=Label(vP, text="Trabajo:",bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    trabajoPotenciaLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    trabajoPotenciaIn=Entry(vP, justify="center")
    trabajoPotenciaIn.grid(row=1,column=1)
    
    tiempoLbl=Label(vP, text="Tiempo:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    tiempoLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    tiempoIn=Entry(vP,justify="center")
    tiempoIn.grid(row=2,column=1)
    
    btn=Button(vP, text="Calcular", command=calculoPotencia)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoPotenciaLbl=Label(vP,text="Resultado:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    resultadoPotenciaLbl.grid(row=3,column=0, padx=10, pady=5,sticky="nsew")
    
    resultadoPotenciaIn=Entry(vP, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoPotenciaIn.grid(row=3,column=1)
    
    mostrarBtn=Button(vP, text="Mostrar Datos", command=mostrarDatosPotencia)
    mostrarBtn.grid(row=4,column=1, pady=10)

#BOTONES MENU PRINCIPAL
#frame de botones
frameBtn=Frame(raiz, bg="#350b4b")
frameBtn.grid()
btn1=Button(frameBtn, text="Teoria de TRABAJO", command = teoriaTrabajo)
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