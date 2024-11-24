from tkinter import *
from tkinter import messagebox
import math

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
    vTF.geometry("400x300+700+400")
    
    #FUNCION QUE CALCULA EL TRABAJO DE UNA FUERZA CONSTANTE
    def calculo():
        f=fuerzaIn.get()
        a=anguloIn.get()
        aRad=math.radians(float(a))
        d=distanciaIn.get()
        r=float(f)*float(d)*math.cos(aRad)
        resultadoIn.config(state="normal")
        resultadoIn.delete(0,"end")
        resultadoIn.insert(0,r)
        resultadoIn.config(state="readonly")
        
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

#BOTONES
btn1=Button(raiz, text="Teoria de TRABAJO")
btn1.grid(row=1,column=0,pady=10)

btn2=Button(raiz, text="Calcular Trabajo de una fuerza constante", command=trabajoC)
btn2.grid(row=2,column=0,pady=10)

btn3=Button(raiz, text="Calcular Trabajo de una fuerza variable")
btn3.grid(row=3,column=0,pady=10)

btn0=Button(raiz, text="Salir del programa", fg="red", command=salir)
btn0.grid(row=4,column=0)

raiz.mainloop()