from tkinter import *
from tkinter import ttk
from gestorAplicacion.usuarios.cliente import Cliente
from gestorAplicacion.transacciones.bolsillo import Bolsillo


class FieldFrame(Frame):
    aux = []
    def __init__(self,tituloCriterios, criterios,tituloValores,valores,habilitado):
        super().__init__()
        self.labelList=[]
        self.entrys=[]
        self.userEntry=[]
        self.place(relx=0.31, rely=0.5, relwidth=0.9,relheight=1)
        self.tituloC=Label(self,text=tituloCriterios,font=("Arial",30),fg="#2C9DF9")
        self.tituloC.grid(row=0,column=0,ipadx=20,sticky=N)
        self.tituloVal=Label(self,text=tituloValores,font=("Arial",30),fg="#2C9DF9")
        self.tituloVal.grid(row=0,column=1,ipadx=20,sticky=N)
        fila=1
        for i in range (len(criterios)):
            if criterios[i] =="Cuenta" or criterios[i]=="Cuenta origen" or criterios[i]=="Cuenta destino":
                
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=ttk.Combobox(self,values=Cliente.listaCuentas,font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1

            elif criterios[i] =="Categoria":
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=ttk.Combobox(self,values=Bolsillo.CATEGORIA,font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1

            elif criterios[i] =="Bolsillo":
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=ttk.Combobox(self,values=Cliente.buscarCuenta(self, FieldFrame.aux[-1]).getMisBolsillos(),font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1

            elif criterios[i] =="Prestamo":
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=ttk.Combobox(self,values=Cliente.buscarCuenta(self, FieldFrame.aux[-1]).getPrestamos(),font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1
            
            elif criterios[i] =="Tipo Movimiento":
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=ttk.Combobox(self,values=["Transferencias","Pagos"],font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1

            elif criterios[i] =="Multa":
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=ttk.Combobox(self,values=Cliente.buscarCuenta(self, FieldFrame.aux[-1]).getMultas(),font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1

            else:
                title=Label(self,text=criterios[i],font=("Arial",25),justify=LEFT)
                self.labelList.append(title)
                title.grid(row=fila,column=0,pady=10)
                entrada=Entry(self,font=("Arial",30))
                self.entrys.append(entrada)
                entrada.grid(row=fila,column=1,pady=10)
                fila+=1

        if valores!= None:
            for i in range(len(valores)):
                self.entrys[i].insert(INSERT,valores[i])

        if habilitado!= None:
            for i in habilitado:
                self.entrys[i].config(state=DISABLED)

        #print(labelList[0].cget("text"))
        self.acceptButton = Button(self,text="Aceptar",font=("Calibri light",20),fg="#764574",bd=5,command=self.aceptar)
        self.acceptButton.grid(row=fila+1,column=0,pady=50)
        self.deleteButton = Button(self,text="Borrar",font=("Calibri light",20),fg="#764574",bd=5,command=self.borrar)
        self.deleteButton.grid(row=fila+1,column=1,pady=50)
    
    def aceptar(self):
        for i in self.entrys:
            self.userEntry.append(i.get())
        return self.userEntry
    def borrar(self):
        for i in self.entrys:
            i.delete(0,last="end")
    @classmethod
    def Metodoaux(cls,opcion):
        FieldFrame.aux.append(opcion)


