from tkinter import *
from tkinter import messagebox
from gestorAplicacion.fieldFrame import FieldFrame
from gestorAplicacion.usuarios.cliente import Cliente
from gestorAplicacion.transacciones.movimiento import Movimiento
from gestorAplicacion.transacciones.bolsillo import Bolsillo
import os
import pathlib


path= os.path.join(pathlib.Path(__file__).parent.absolute())
cliente1=Cliente("santiago",1201823)
class ventanaUno(Tk):
    count=0
    def __init__(self):
        super().__init__()
        self.title("Ventana Inicio")
        self.geometry("500x500")
        self.state('zoomed')
        def descripcion():
            bienvenida_lbl.config(text="Piggy Bank es una aplicación bancaria que permite\nrealizar prestamos y realizar el pago de los mismos, \ngenerar un ahorro por medio de la opción bolsillos y permite \nllevar el control de los movimientos generados en la cuenta",font=("Arial",15))

        
        #Frames

        frame1=Frame(self,border=2,borderwidth=2)
        frame1.place(relheight=0.96,relwidth=0.47,rely=0.02,relx=0.02,anchor=NW)
        frame2 = Frame(self)
        frame2.place(relheight=0.96,relwidth=0.47,rely=0.02,relx=0.51)

        #Menu
        menuBar=Menu(self)
        menu1=Menu(menuBar)
        self.config(menu=menuBar)
        menuBar.add_cascade(label="Inicio",foreground="blue",menu=menu1)
        menu1.add_cascade(label="Descripción ",command=descripcion)
        menu1.add_cascade(label="Salir",command=self.destroy)

        #Saludo

        frameBienvenida=Frame(frame1)
        frameBienvenida.place(rely=0.01,relx=0.02,relwidth=0.96,relheight=0.3)
        bienvenida_lbl = Label(frameBienvenida,text="Bienvenido a PiggyBank \nLa app que te permite mover tu dinero\nde forma rápida y segura",font=("Arial",15),borderwidth=3,relief=SOLID)
        bienvenida_lbl.place(rely=0.01,relx=0.02,relwidth=0.98,relheight=0.98)


        #Ingreso

        frameIngreso=Frame(frame1)
        frameIngreso.place(rely=0.33,relx=0.02,relwidth=0.96,relheight=0.66)
        botonIngreso=Button(frameIngreso,text="Iniciar PiggyBank",font=("Calibri light",30),fg="#5F3A8F",command=self.principal)
        botonIngreso.pack(side="bottom",fill='x')
        
        self.ingresoimgList=['./fotos/prestamos.png','/fotos/pagos.png', '/fotos/movimientos.png', '/fotos/bolsillos.png','./fotos/transferencias.png']
        self.ingresoIndex=0
        def switchimage(evento):
            self.ingresoIndex+=1
            if self.ingresoIndex>4:
                self.ingresoIndex=0
                fotosingreso.config(file=path+"\\fotos\\logo.png")
            else:
                fotosingreso.config(file=path+self.ingresoimgList[self.ingresoIndex])

        labelimagenIngreso=Label(frameIngreso)
        fotosingreso = PhotoImage(file=path+"\\fotos\\logo.png")
        labelimagenIngreso.config(image=fotosingreso)
        labelimagenIngreso.bind('<Enter>',switchimage)
        labelimagenIngreso.pack(side=TOP,fill="y",pady=20)
        
        #Nombres y cambios
        self.frameCv=Frame(frame2,borderwidth=2,relief=SOLID)
        self.frameCv.place(rely=0.01,relx=0.02,relwidth=0.96,relheight=0.3)
        devslist=["Valentina Ospina Narvaez \n""24 años \n""Programa: Ingeniería de sistemas e Informática",
        "Santiago Varela Vanegas \n""26 años \n" "Programa: Ingeniería de sistemase e Informática",
        "Sofia Andrade  \n""22 años \n""Programa: Ingeniería de sistemas e Informática",
        "Kevin Arias \n""21 años \n""Programa: Ingeniería de sistemas e Informática"]
        self.devIndex=0
        self.fotosIndex=0
        self.devslbl=StringVar()
        self.devslbl.set(devslist[self.devIndex])

        def mostrarDevs(evento):
            self.devIndex+=1
            self.fotosIndex+=4
            if self.devIndex==4:
                self.devIndex=0
                self.devslbl.set(devslist[0])
                
            else:
                self.devslbl.set(devslist[self.devIndex])
            if self.fotosIndex>15:
                self.fotosIndex=0
                fotos.config(file=path+self.ubic[self.fotosIndex])
                fotos2.config(file=path+self.ubic[self.fotosIndex+1])
                fotos3.config(file=path+self.ubic[self.fotosIndex+2])
                fotos4.config(file=path+self.ubic[self.fotosIndex+3])
            else:
                fotos.config(file=path+self.ubic[self.fotosIndex])
                fotos2.config(file=path+self.ubic[self.fotosIndex+1])
                fotos3.config(file=path+self.ubic[self.fotosIndex+2])
                fotos4.config(file=path+self.ubic[self.fotosIndex+3])
        


            
            
        self.cv_lbl = Label(self.frameCv,textvariable=self.devslbl,font=("Arial",20))
        self.cv_lbl.bind('<ButtonPress-1>', mostrarDevs)
        self.cv_lbl.place(relwidth=1,relheight=1)

        #fotos
        framePhotos=Frame(frame2,borderwidth=2,relief=SOLID)
        self.ubic = ['./fotos/V1.png','/fotos/V2.png', '/fotos/V3.png', '/fotos/V4.png',
                    './fotos/S1.png', './fotos/S2.png','./fotos/S3.png', './fotos/S4.png',
                    './fotos/SO1.png', './fotos/SO2.png','./fotos/SO3.png', './fotos/SO4.png',
                    './fotos/K1.png','./fotos/K2.png','./fotos/K3.png', './fotos/K4.png']

        framePhotos.place(rely=0.33,relx=0.02,relwidth=0.96,relheight=0.66)
        self.labelimagen1=Label(framePhotos)
        fotos = PhotoImage(file=path+self.ubic[0])
        self.labelimagen1.config(image=fotos)
        self.labelimagen1.grid(row=0,column=0,sticky="n")

        labelimagen2=Label(framePhotos)
        fotos2 = PhotoImage(file=path+self.ubic[1])
        labelimagen2.config(image=fotos2)
        labelimagen2.grid(row=0,column=1,sticky="n",ipadx=5)

        labelimagen3=Label(framePhotos)
        fotos3 = PhotoImage(file=path+self.ubic[2])
        labelimagen3.config(image=fotos3)
        labelimagen3.grid(row=1,column=0,sticky="n")

        labelimagen4=Label(framePhotos)
        fotos4 = PhotoImage(file=path+self.ubic[3])
        labelimagen4.config(image=fotos4)
        labelimagen4.grid(row=1,column=1,sticky="n",ipadx=5)

        self.mainloop()

    def principal(self):
        self.destroy()
        ventanaMenu()
    

class ventanaMenu(Tk):

    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("1000x900")
        self.state('zoomed')
        def prestamo():
            self.titulo.config(text="Prestamo")
            self.descripcion.config(text="Puedes solicitar un prestamo entre 500.000 y 7'000.000 a 24 cuotas")
            self.datos=FieldFrame("Información",["Valor","Cuenta","Tipo de prestamo"],"Datos",[],[])
            
            #print(cliente1.listaCuentas[3].getId())
            def solicitarPrestamo(evento):
                self.informacion=self.datos.aceptar()
                id=(self.datos.userEntry[1]).strip().split(" ")
                cliente1.solicitarPrestamo(int(self.datos.userEntry[0]),self.datos.userEntry[2],int(id[5]))
                messagebox.showinfo("informacion del prestamo",cliente1.buscarCuenta(int(id[5])).prestamos[-1].mensajePrestamo())
            self.datos.acceptButton.bind('<Button-1>',solicitarPrestamo)
            
        
        def bolsillos():
            self.titulo.config(text="Bolsillo")
            self.descripcion.config(text="Creatu Bolsillo con 3 sencillos pasos")
            self.datos=FieldFrame("Información",["Cuenta","Categoria","Meta de ahorro"],"Datos",[],[])

            def generarAhorro(evento):
                self.informacion=self.datos.aceptar()
                id=(self.datos.userEntry[0]).strip().split(" ")
                categoria = self.datos.userEntry[1]
                cliente1.generarAhorro(int(self.datos.userEntry[2]),Bolsillo.CATEGORIA.index(categoria),int(id[5]))
                messagebox.showinfo("informacion del bolsillo",cliente1.buscarCuenta(int(id[5])).misBolsillos[-1].mensajeBolsillo())
            self.datos.acceptButton.bind('<Button-1>',generarAhorro)

        def Cargarbolsillo():
            self.titulo.config(text="Cargar Bolsillo")
            self.descripcion.config(text="Ya tienes tu bolsillo creado?\nPues empieza a ahorrar")
            self.datos=FieldFrame("Información",["Cuenta"],"Datos",[],[])
            def selectBolsillo(evento):
                self.informacion=self.datos.aceptar()
                idCuenta=(self.datos.userEntry[0]).strip().split(" ")[5]
                FieldFrame.Metodoaux(int(idCuenta))
                self.datos=FieldFrame("Información", ["Bolsillo","Valor"],"Datos",[],[])
                def numBolsillo(evento):
                    self.informacion=self.datos.aceptar()
                    idBolsillo=(self.datos.userEntry[0]).strip().split(" ")[1][0]

                    messagebox.showinfo("informacion del Bolsillo",cliente1.cargarAhorro(int(idCuenta),int(idBolsillo),int(self.datos.userEntry[1])))
                self.datos.acceptButton.bind('<Button-1>',numBolsillo)
            self.datos.acceptButton.bind('<Button-1>',selectBolsillo)

        def Descargarbolsillo():
            self.titulo.config(text="Descargar Bolsillo")
            self.descripcion.config(text="puedes descargar tu bolsillo al toque mi rey") 
            self.datos=FieldFrame("Información",["Cuenta"],"Datos",[],[])
            def selectBolsillo(evento):
                self.informacion=self.datos.aceptar()
                idCuenta=(self.datos.userEntry[0]).strip().split(" ")[5]
                FieldFrame.Metodoaux(int(idCuenta))
                self.datos=FieldFrame("Información", ["Bolsillo","Valor"],"Datos",[],[])
                def numBolsillo(evento):
                    self.informacion=self.datos.aceptar()
                    idBolsillo=(self.datos.userEntry[0]).strip().split(" ")[1][0]

                    messagebox.showinfo("informacion del Bolsillo",cliente1.descargarAhorro(int(idCuenta),int(idBolsillo),int(self.datos.userEntry[1])))
                self.datos.acceptButton.bind('<Button-1>',numBolsillo)
            self.datos.acceptButton.bind('<Button-1>',selectBolsillo)

        
        def transferencia():
            self.titulo.config(text="Transferencia")
            self.descripcion.config(text="Transferencias entre tus cuentas\nPuedes ahora interactuar entre tus saldos")
            self.datos=FieldFrame("Información",["Cuenta origen","Cuenta destino","Valor transferencia"],"Datos",[],[])

            def trasferir(evento):
                self.informacion=self.datos.aceptar()
                idOrigen = (self.datos.userEntry[0]).strip().split(" ")
                idDestino = (self.datos.userEntry[1]).strip().split(" ")
                valor = int(self.datos.userEntry[2])
                messagebox.showinfo("Información de la transferencia",cliente1.hacerTransferencia(int(idOrigen[5]), int(idDestino[5]), valor))
            self.datos.acceptButton.bind('<Button-1>',trasferir)


        def movimientos():
            self.titulo.config(text="Movimientos")
            self.descripcion.config(text="Resvisa tu historial de Movimientos\nLLeva un control de todo lo que haz hecho en tu cuenta")
            self.datos=FieldFrame("Información",["Cuenta","Tipo Movimiento"],"Datos",[],[])
            def movimiento(evento):
                self.informacion=self.datos.aceptar()
                idCuenta=(self.datos.userEntry[0]).strip().split(" ")[5]
                metodo = (self.datos.userEntry[1]).strip()
                if metodo == "Transferencias":
                    lista = Cliente.movimientoTransferencia(idCuenta)
                    print (lista)
                    messagebox.showinfo("Información de las transferencias",)
    
                else:
                    lista = Cliente.movPago(idCuenta)
                    print(lista)

                    messagebox.showinfo("Información de los Pagos",)
            self.datos.acceptButton.bind('<Button-1>',movimiento)


        def pagoPrestamo():
            
            self.titulo.config(text="Pago")
            self.descripcion.config(text="realiza ya tu pago de prestamo, ¿que esperas!\nPaga hasta 24 cuotas!")
            self.datos=FieldFrame("Información",["Cuenta origen"],"Datos",[],[])
            def selectPrestamo(evento):
                self.informacion=self.datos.aceptar()
                idCuenta=(self.datos.userEntry[0]).strip().split(" ")[5]
                FieldFrame.Metodoaux(int(idCuenta))
                #cliente1.solicitarPrestamo(924723,"libre",int(idCuenta))

                self.datos=FieldFrame("Información", ["Prestamo","Cuotas de pago"],"Datos",[],[])
                def numPrestamo(evento):
                    self.informacion=self.datos.aceptar()
                    idPrestamo=(self.datos.userEntry[0]).strip().split(":")[0]

                    messagebox.showinfo("informacion del Pago",cliente1.hacerPagoPrestamo(int(idCuenta),int(idPrestamo),int(self.datos.userEntry[1])))
                self.datos.acceptButton.bind('<Button-1>',numPrestamo)
            self.datos.acceptButton.bind('<Button-1>',selectPrestamo)
            
        
        def pagoMulta():
            
            self.titulo.config(text="Pago")
            self.descripcion.config(text="realiza ya tu pago de multa\n¿que esperas!")
                
            self.datos=FieldFrame("Información",["Cuenta origen"],"Datos",[],[])
            def selectMulta(evento):
                self.informacion=self.datos.aceptar()
                idCuenta=(self.datos.userEntry[0]).strip().split(" ")[5]
                FieldFrame.Metodoaux(int(idCuenta))
                self.datos=FieldFrame("Información", ["Multa","Cuotas de pago"],"Datos",[],[])
                def numMulta(evento):
                    self.informacion=self.datos.aceptar()
                    idMulta=(self.datos.userEntry[0]).strip().split(":")[0]

                    messagebox.showinfo("informacion del Pago",cliente1.hacerPagoMulta(int(idCuenta),int(idMulta),int(self.datos.userEntry[1])))
                self.datos.acceptButton.bind('<Button-1>',numMulta)
            self.datos.acceptButton.bind('<Button-1>',selectMulta)
    
        
        def aplicacioninfo():
            messagebox.showinfo("Piggy Bank","Una aplicacion bancaria dedicada al manejo de finanzas, podras realizar prestamos, generar pagos, realizar transferencias, generar bolsillos y verificar los movimientos realizados en cada operación")
        
        def acercaDeInfo():
            messagebox.showinfo("Desarrolladores","Valentina Ospina Narvaez \nSantiago Varela Vanegas \nSofia Andrade Palacio \nKevin Leonardo Arias Orrego")

        self.titulo=Label(self,font=("Arial",30))
        self.titulo.place(relwidth=1,rely=0.03)
        self.descripcion=Label(self,font=("Arial",20))
        self.descripcion.place(relwidth=1,rely=0.2,relheight=0.20)

        
        self.menuBar = Menu(self)
        self.config(menu=self.menuBar)
        menuArchivo = Menu(self.menuBar,activebackground="blue",activeforeground="white")
        self.menuBar.add_cascade(label="Archivo", menu=menuArchivo)
        menuArchivo.add_command(label="Aplicacion",command=aplicacioninfo)
        menuArchivo.add_command(label="Salir",command=self.volver)
        menuProcesos=Menu(self.menuBar)
        self.menuBar.add_cascade(label="Procesos y Consultas",menu=menuProcesos)

        #Manu Prestamos
        menuProcesos.add_command(label="Prestamo",command=prestamo)

        #Menu Bolsillos
        menuBolsillos=Menu(self.menuBar)
        menuProcesos.add_cascade(label="Bolsillos",menu=menuBolsillos)
        menuBolsillos.add_command(label="Generar Bolsillo",command=bolsillos)
        menuBolsillos.add_command(label="Cargar Bolsillo",command=Cargarbolsillo)
        menuBolsillos.add_command(label="Descargar Bolsillo",command=Descargarbolsillo)

        #Menu Transferencias
        menuProcesos.add_command(label="Transferencia",command=transferencia)

        #Menu Movimientos
        menuProcesos.add_command(label="Movimientos",command=movimientos)

        #menuPagos
        menuPagos=Menu(self.menuBar)
        menuProcesos.add_cascade(label="Pagos",menu=menuPagos)
        menuPagos.add_command(label="Pago Prestamo",command=pagoPrestamo)
        menuPagos.add_command(label="Pago multa",command=pagoMulta)

        menuAyuda=Menu(self.menuBar)
        self.menuBar.add_cascade(label="Ayuda",menu=menuAyuda)
        menuAyuda.add_command(label="Acerca de",command=acercaDeInfo)
        self.mainloop()

    def volver(self):
        self.destroy()
        ventanaUno()
ventanaUno()
