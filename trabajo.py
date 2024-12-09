from tkinter import *
from tkinter import messagebox
import math
import webbrowser
import matplotlib.pyplot as plt
import numpy as np
import ctypes
from scipy.integrate import trapezoid
#ARREGLOS
#arreglos de trabajo de fuerza variable
ecuacion=[]
limiteInf=[]
limiteSup=[]
trabajoV=[]
datosTFV=[ecuacion,limiteInf,limiteSup,trabajoV]
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

#arreglos de trabajo del resorte
constante=[]
xInicial=[]
xFinal=[]
trabajoR=[]
datosResorte = [constante, xInicial, xFinal, trabajoR]

#CONFIGURACIONES VENTANA PRINCIPAL
raiz=Tk()
raiz.iconbitmap("work.ico")
raiz.title("TRABAJO")
raiz.config(bg="#350b4b")
raiz.resizable("False","False")

#DIMENSIONES DE LA VENTANA
ancho_ventana = 400
alto_ventana = 630

#OBTENER DIMENSIONES DE LA PANTALLA
user32 = ctypes.windll.user32
ancho_pantalla = user32.GetSystemMetrics(0)
alto_pantalla = user32.GetSystemMetrics(1)

#CALCULAR COORDENADAS PARA CENTRAR LA VENTANA
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y-30}")
mainImage=PhotoImage(file="work.png")

titulo= Label(raiz, text ="CALCULO DEL TRABAJO", bg = "#F4D03F", fg = "#ffffff", font=("Impact", 20, "bold"))
titulo.grid(row=1,column=0,pady=10)
#frame de la imagen
frameImg=Frame(raiz,bg="#350b4b")
frameImg.grid(row=0,column=0,pady=12)
imgLbl=Label(frameImg,image=mainImage,bg="#350b4b")
imgLbl.grid(row=0,column=0,padx=73)

def salir():
    valor=messagebox.askokcancel("Salir","Estas seguro que deseas salir?")
    if valor==True:
        raiz.destroy()

#VENTANA DE TEORIA DE TRABAJO
def teoriaTrabajo():
    teoria = Toplevel(raiz)
    teoria.title("Teoria")
    teoria.iconbitmap("work.ico")
    teoria.geometry("280x300+670+200")
    teoria.resizable(0,0)
    teoria.config(bg = "#350b4b")
    frameBtn=Frame(teoria, bg="#350b4b")
    frameBtn.grid()
    
    def verEnLinea():
        url = "https://csmer.uprrp.edu/wp-content/uploads/Trabajo-Potencia-y-Maquinas-Simples.pdf"
        url1 = "https://fisica.uprb.edu/cursos/FISI3173VK1/Teoria6.pdf"
        try:
            webbrowser.open(url, new=2) 
            webbrowser.open(url1, new=3) 
        except ValueError:
            messagebox.showerror("Error", "No se pudo abrir en linea, revise su conexion a internet")

    def descargarLibro():
        urlLum = "https://drive.google.com/uc?export=download&id=1Yjke8ePblaCpMXQvqJP8tQt64fDqwjgb"    
        try:
            webbrowser.open(urlLum, new=2)
        except ValueError:
            messagebox.showerror("ERROR" , "No se pudo realizar la descarga")

    def verClase():
        urlTeoClase = "https://drive.google.com/file/d/1Te-puR3r3tkcSgz4PGKi-wGc2pjfsGcZ/view?usp=sharing"
        try:
            webbrowser.open(urlTeoClase, new=2)
        except ValueError:
            messagebox.showerror("ERROR", "No se puedo abrir el archivo, revise la conexion a internet")

    def downloadTeo():
        urlTeoClase = "https://drive.google.com/uc?export=download&id=1Te-puR3r3tkcSgz4PGKi-wGc2pjfsGcZ"
        try:
            webbrowser.open(urlTeoClase, new=2)
        except ValueError:
            messagebox.showerror("ERROR", "No se puedo abrir el archivo, revise la conexion a internet")

    #MENU
    tituloTeoria = Label(frameBtn, text ="BIENVENIDO A TEORIA", bg = "#F4D03F", fg = "#ffffff", font=("Impact", 20, "bold"))
    tituloTeoria.grid(row=0,column=0,pady=25,padx=15)
    btn1=Button(frameBtn, text="Ver teoria en linea" ,bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"), command = verEnLinea)
    btn1.grid(row=1,column=0,pady=10)
    btn1=Button(frameBtn, text="Ver teoria en clase",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"), command = verClase)
    btn1.grid(row=2,column=0,pady=10)
    btn1=Button(frameBtn, text="Descargar teoria en clase",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"),command = downloadTeo)
    btn1.grid(row=3,column=0,pady=10)
    btn1=Button(frameBtn, text="Descargar libro de fisica",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"), command= descargarLibro)
    btn1.grid(row=4,column=0,pady=10)
#VENTANA DE LA OPCION TRABAJO VARIABLE
def trabajoV():

    vTV=Toplevel(raiz)
    
    def escenaPrincipal():
        vTV.title("Fuerza variable")
        vTV.geometry("330x300+750+400")
        vTV.resizable(0,0)
        vTV.config(bg="#F4D03F")
        
        
        frameLista.grid_forget()
        frameT1.grid()
        
        
        
    def mostrarDatos():
        if len(datosTFV[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vTV.destroy()
            return
        
        vTV.title("Datos")
        vTV.geometry("590x400+100+300")
        vTV.resizable(0,0)
        vTV.config(bg= "#F4D03F")
        
        frameT1.grid_forget()
        frameLista.grid(padx=2)
        volverBtn.grid(row=len(datosTFV[0])+2,column=3, pady=20)
        
        #Entrys
        
        for i in range(len(datosTFV[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosTFV[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosTFV[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosTFV[2][i])
            dIn.config(state="readonly")
            
            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+2,column=3)
            tIn.insert(0,datosTFV[3][i])
            tIn.config(state="readonly")
            
    def calculo():
        
        def f(x):
            return eval(ecua)
        
        def procesar_funcion(equacion):
            funciones = ["sin", "cos", "tan", "exp", "log", "sqrt"]
            for func in funciones:
                equacion = equacion.replace(func, f"np.{func}")
            return equacion
        
        ecua=ecuacionIn.get()
        datosTFV[0].append(ecua)
        ecua=procesar_funcion(ecua)
        
        limIn=float(limiteInfIn.get())
        limSup=float(limiteSupIn.get())
        
        datosTFV[1].append(limIn)
        datosTFV[2].append(limSup)
        
        x_plot=np.linspace(-2*limSup,2*limSup,500)
        y_plot=f(x_plot)

        x=np.linspace(limIn,limSup,200)
        y=f(x)
        
        t=round(trapezoid(y,x),3)
        datosTFV[3].append(t)
            
        resultadoIn.config(state="normal")
        resultadoIn.delete(0,"end")
        resultadoIn.insert(0,t)
        resultadoIn.config(state="readonly")
        
        plt.gcf().canvas.manager.set_window_title("Fuerza vs Posicion")
        plt.get_current_fig_manager().window.geometry("+60+240") 
        
        plt.axhline(0, color='black', linewidth=1)  # Eje X
        plt.axvline(0, color='black', linewidth=1)  # Eje Y
        
        plt.title("Fuerza vs Posicion")
        plt.axis([-2*limSup,2*limSup,-3*limSup,3*limSup])
        plt.plot(x_plot,y_plot, color="red", label="f(x)")
        plt.fill_between(x,y,color="purple",alpha=0.5, label="Trabajo")
        plt.legend()
        plt.xlabel("Posicion (m)")
        plt.ylabel("Fuerza (N)")
        plt.grid(alpha=0.3)
        plt.show()
    
    #ESCENA PRINCIPAL-----------------------------------------------------------------------------------------
    frameT1=Frame(vTV,bg="#F4D03F")
    
    tituloLbl=Label(frameT1, text="TRABAJO DE UNA \nFUERZA VARIABLE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloLbl.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")
    
    ecuacionLbl=Label(frameT1, text="Ecuacion:",bg= "#F4D03F" ,fg = "#ffffff", font=("Arial",11,"bold"))
    ecuacionLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    ecuacionIn=Entry(frameT1, justify="center")
    ecuacionIn.grid(row=1,column=1)
    
    limiteInfLbl=Label(frameT1, text="Limite inferior:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    limiteInfLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    limiteInfIn=Entry(frameT1,justify="center")
    limiteInfIn.grid(row=2,column=1)
    
    limiteSupLbl=Label(frameT1, text="Limite superior:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    limiteSupLbl.grid(row=3,column=0, sticky="nsew", padx=10,pady=5)
    
    limiteSupIn=Entry(frameT1,justify="center")
    limiteSupIn.grid(row=3,column=1)
    
    btn=Button(frameT1, text="Calcular", command=calculo)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoLbl=Label(frameT1,text="Trabajo:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    resultadoLbl.grid(row=4,column=0,sticky="nsew", padx=10, pady=5)
    
    resultadoIn=Entry(frameT1, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoIn.grid(row=4,column=1)
    
    mostrarBtn=Button(frameT1, text="Mostrar Datos", command=mostrarDatos)
    mostrarBtn.grid(row=5,column=1, pady=20)
    
    #SEGUNDA ESCENA---------------------------------------------------------------------------------------------------
    frameLista=Frame(vTV, bg= "#F4D03F")

    tituloHistorial=Label(frameLista, text="HISTORIAL DE TRABAJO", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorial.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

    fLbl=Label(frameLista, text="Ecuacion", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    fLbl.grid(row=1,column=0, padx=10, pady=5)
        
    aLbl=Label(frameLista, text="Lim. Inferior",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    aLbl.grid(row=1,column=1, padx=10, pady=5)
        
    dLbl=Label(frameLista, text="Lim. Superior",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    dLbl.grid(row=1,column=2, padx=10,pady=5)
        
    tLbl=Label(frameLista,text="Trabajo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    tLbl.grid(row=1,column=3, padx=10, pady=5)
    
    volverBtn=Button(frameLista, text="volver", command=escenaPrincipal)
        
    escenaPrincipal()
    
    
    
    
#VENTANA DE LA OPCION TRABAJO CONSTANTE
def trabajoC():
    vTF=Toplevel(raiz)
            
    def escenaPrincipal():
        vTF.iconbitmap("work.ico")
        vTF.title("Fuerza constante")
        vTF.geometry("330x300+780+400")     
        vTF.config( bg= "#F4D03F")
        vTF.resizable(0,0)
    
        frameLista.grid_forget()
        frameEnt.grid(padx=10,pady=5)
        
    def mostrarDatos():
        if len(datosTFC[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vTF.destroy()
            return
        
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
            
        
        vTF.title("Datos")
        vTF.geometry("590x400+650+350")
        vTF.resizable(0,0)
        vTF.config( bg= "#F4D03F")
        
        frameEnt.grid_forget()
        frameLista.grid(padx=2)
        volverBtn.grid(row=len(datosTFC[0])+2,column=3, pady=20)

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

    
    #PRIMERA ESCENA------------------------------------------------------------------------------------------
    frameEnt=Frame(vTF, bg= "#F4D03F")
    
    tituloHistorial = Label(frameEnt, text="TRABAJO DE UNA \nFUERZA CONSTANTE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
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
    
    #SEGUNDA ESCENA---------------------------------------------------------------------------------------------
    frameLista=Frame(vTF, bg= "#F4D03F")

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
    
    volverBtn=Button(frameLista, text="volver", command=escenaPrincipal)
        
    escenaPrincipal()

#VENTANA DE LA OPCION POTENCIA
def potencia():
    vP=Toplevel(raiz)
    
    def escenaPrincipal():
        
        vP.iconbitmap("work.ico")
        vP.title("Potencia")
        vP.geometry("320x210+790+440")
        vP.resizable(0,0)
        vP.config(bg="#F4D03F")
        
        frameLista.grid_forget()
        frame1.grid(padx=10,pady=5)
    
    def mostrarDatosPotencia():
        
        if len(datosPot[0])==0:
                messagebox.showerror("ERROR","No hay datos para visualizar")
                vP.destroy()
                return

        vP.title("Datos")
        vP.geometry("440x400+730+330")
        vP.config(bg= "#F4D03F")
        vP.resizable(0,0)
        
        frame1.grid_forget()
        frameLista.grid(padx=2)
        volverBtn.grid(row=len(datosPot[0])+2,column=2, pady=20)
       
        
        #Entrys
        
        for i in range(len(datosPot[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosPot[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosPot[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosPot[2][i])
            dIn.config(state="readonly")
            
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
    
    

    #ESCENA PRINCIPAL-------------------------------------------------------------------------------------------------------------
    frame1=Frame(vP,bg="#F4D03F")
    tituloPotencia = Label(frame1, text="  POTENCIA", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloPotencia.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    trabajoPotenciaLbl=Label(frame1, text="Trabajo:",bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    trabajoPotenciaLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    trabajoPotenciaIn=Entry(frame1, justify="center")
    trabajoPotenciaIn.grid(row=1,column=1)
    
    tiempoLbl=Label(frame1, text="Tiempo:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    tiempoLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    tiempoIn=Entry(frame1,justify="center")
    tiempoIn.grid(row=2,column=1)
    
    btn=Button(frame1, text="Calcular", command=calculoPotencia)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoPotenciaLbl=Label(frame1,text="Resultado:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    resultadoPotenciaLbl.grid(row=3,column=0, padx=10, pady=5,sticky="nsew")
    
    resultadoPotenciaIn=Entry(frame1, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoPotenciaIn.grid(row=3,column=1)
    
    mostrarBtn=Button(frame1, text="Mostrar Datos", command=mostrarDatosPotencia)
    mostrarBtn.grid(row=4,column=1, pady=10)
    
    #SEGUNDA ESCENA------------------------------------------------------------------------------------------------------
    frameLista=Frame(vP,bg= "#F4D03F")
    tituloHistorialPotencia = Label(frameLista, text="HISTORIAL DE POTENCIA", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorialPotencia.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    fLbl=Label(frameLista, text="Trabajo", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    fLbl.grid(row=1,column=0, padx=10, pady=5)
        
    aLbl=Label(frameLista, text="Tiempo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    aLbl.grid(row=1,column=1, padx=10, pady=5)
        
    dLbl=Label(frameLista, text="Potencia",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    dLbl.grid(row=1,column=2, padx=10,pady=5)
    
    volverBtn=Button(frameLista, text="volver", command=escenaPrincipal)
        
    escenaPrincipal()
    
#VENTANA DE LA OPCION TRABAJO DE RESORTE
def trabajoR():
    vR = Toplevel(raiz)
    
    def escenaPrincipal():
        vR.iconbitmap("work.ico")
        vR.title("Trabajo Resorte")
        vR.geometry("330x300+780+400")
        vR.resizable(0, 0)
        vR.config(bg="#F4D03F")
        
        frameLista.grid_forget()
        frameEnt.grid(padx=10,pady=5)
        
    
    def mostrarDatosResorte():
        if len(datosResorte[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vR.destroy()
            return
        
        vR.title("Datos")
        vR.geometry("590x400+660+330")
        vR.config(bg= "#F4D03F")
        vR.resizable(0,0)
        
        frameEnt.grid_forget()
        frameLista.grid(padx=2)
        volverBtn.grid(row=len(datosResorte[0])+2,column=3, pady=20)
        
        for i in range(len(datosResorte[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosResorte[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosResorte[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosResorte[2][i])
            dIn.config(state="readonly")

            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+2,column=3, padx=10)
            tIn.insert(0,datosResorte[3][i])
            tIn.config(state="readonly")
        

    #FUNCION PARA CALCULAR TRABAJO DEL RESORTE
    def calculoResorte():
        try:

            k = float(constanteIn.get())
            xi = float(xInicialIn.get())
            xf = float(xFinalIn.get())
            if k <= 0:
                messagebox.showerror("Error", "La constante no puede ser negativa")
                return
            w=round(0.5 * k *( xf**2 - xi**2), 4)
            datosResorte[0].append(k)
            datosResorte[1].append(xi)
            datosResorte[2].append(xf)
            datosResorte[3].append(w)

            resultadoTrabajoIn.config(state="normal")
            resultadoTrabajoIn.delete(0,"end")
            resultadoTrabajoIn.insert(0,w)
            resultadoTrabajoIn.config(state="readonly")
        
        except ValueError:
            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
        
        

    #ESCENA PRINCIPAL-----------------------------------------------------------------------------------
    frameEnt=Frame(vR, bg= "#F4D03F")
    

    tituloHistorialResorte = Label(frameEnt, text="TRABAJO DE UN RESORTE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorialResorte.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    constanteLbl=Label(frameEnt, text="Constante:",bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    constanteLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    constanteIn=Entry(frameEnt, justify="center")
    constanteIn.grid(row=1,column=1)
    
    xInicialLbl=Label(frameEnt, text="x Inicial:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    xInicialLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    xInicialIn=Entry(frameEnt,justify="center")
    xInicialIn.grid(row=2,column=1)

    xFinalLbl=Label(frameEnt, text="x final:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    xFinalLbl.grid(row=3,column=0, sticky="nsew", padx=10, pady=5)
    
    xFinalIn=Entry(frameEnt,justify="center")
    xFinalIn.grid(row=3,column=1)
    
    btn=Button(frameEnt, text="Calcular", command=calculoResorte)
    btn.grid(row=3,column=2, padx=10)
    
    resultadoTrabajoLbl=Label(frameEnt,text="Resultado:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    resultadoTrabajoLbl.grid(row=5,column=0, padx=10, pady=5,sticky="nsew")
    
    resultadoTrabajoIn=Entry(frameEnt, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoTrabajoIn.grid(row=5,column=1)
    
    mostrarBtn=Button(frameEnt, text="Mostrar Datos", command=mostrarDatosResorte)
    mostrarBtn.grid(row=6,column=1, pady=10)   
    
    #SEGUNDA ESCENA-----------------------------------------------------------------------------------------------------
    frameLista=Frame(vR, bg= "#F4D03F")
    
    tituloHistorialResorte = Label(frameLista, text=" HISTORIAL DE TRABAJO", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorialResorte.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    fLbl=Label(frameLista, text="Constante", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    fLbl.grid(row=1,column=0, padx=10, pady=5)
        
    aLbl=Label(frameLista, text="x inicial",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    aLbl.grid(row=1,column=1, padx=10, pady=5)
        
    dLbl=Label(frameLista, text="x final",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    dLbl.grid(row=1,column=2, padx=10,pady=5)

    tLbl=Label(frameLista, text="Trabajo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
    tLbl.grid(row=1,column=3, padx=10,pady=5)
    
    volverBtn=Button(frameLista, text="volver", command=escenaPrincipal)
        
    escenaPrincipal()

#BOTONES MENU PRINCIPAL
#frame de botones
frameBtn=Frame(raiz, bg="#350b4b")
frameBtn.grid()
btn1=Button(frameBtn, text="Teoria de TRABAJO", command = teoriaTrabajo)
btn1.grid(row=1,column=0,pady=10)

btn2=Button(frameBtn, text="Calcular Trabajo de una fuerza constante", command=trabajoC)
btn2.grid(row=2,column=0,pady=10)

btn3=Button(frameBtn, text="Calcular Trabajo de una fuerza variable", command=trabajoV)
btn3.grid(row=3,column=0,pady=10)

btn4=Button(frameBtn, text="Calcular Potencia", command=potencia)
btn4.grid(row=4,column=0,pady=10)

btn5=Button(frameBtn, text="Calcular Trabajo de Resorte", command=trabajoR)
btn5.grid(row=5,column=0,pady=10)

btn0=Button(frameBtn, text="Salir del programa", fg="red", command=salir)
btn0.grid(row=6,column=0,pady=10)


raiz.mainloop()