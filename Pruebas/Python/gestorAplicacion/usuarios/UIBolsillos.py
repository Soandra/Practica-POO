from cliente import Cliente
from bolsillo import Bolsillo
from uiMenu import UiMenu


class UIBolsillos:
    @classmethod
    def bolsillo(cls, cliente):
        print("Selecciona una de las opciones disponibles para bolsillos")
        print("""
        1. Generar Bolsillo
        2. Cargar Bolsillo
        3. Descargar Bolsillo""")

        opcionBolsillos = int(input())
        if(opcionBolsillos < 1 or opcionBolsillos > 3):
            print("Opción no valida")
            return

        UiMenu.traerCuentas()
        print("Selecciona la cuenta para generar el ahorro")
        cuenta = int(input())
        if cuenta < len(Cliente.listaCuentas):
            if opcionBolsillos == 1:
                print("Cuánto deseas ahorrar en este bolsillo")
                valorAhorro = int(input())
                print("Ingresa el número correspondiente al tipo de bolsillo que deseas generar")
                print("""
                0. VIAJES          1. EDUCACION     2. SALUD
                3  ALIMENTACION    4  TRANSPORTE    5  HOGAR
                6  IMPREVISTOS     7  OTROS """)
                categoria = int(input())

                if categoria < len(Bolsillo.CATEGORIA):
                    cliente.generarAhorro(valorAhorro, categoria, cuenta)
                    bolsillo = cliente.listaCuentas[cuenta-1].getMisBolsillos()
                    print(bolsillo[-1].mensajeBolsillo())
                
            elif opcionBolsillos == 2:
                print("Selecciona el bolsillo al cual deseas ingresar un monto")
                UiMenu.traerBolsillos(cuenta)
                op1 = int(input())   
                print("1.Carga completa")
                print("2.Carga parcial")
                opcion1 = int(input())

                if( opcion1 < 1 or opcion1 >2):
                    print("Opción no valida")
                    return

                if (opcion1 == 1):
                    print(cliente.cargarAhorro(cuenta, op1))
                elif (opcion1 == 2):            
                    print(" Valor a cargar de tu bolsillo")
                    valorCarga = int(input())
                    print(cliente.cargarAhorro(cuenta, op1, valorCarga))
                else:
                    print("Opción no valida")
                            
            elif opcionBolsillos == 3:
                print("selecciona tu bolsillo")
                UiMenu.traerBolsillos(cuenta)
                op1 = int(input())
                if op1 > len(Cliente.buscarCuenta(op1).misBolsillos) or len(Cliente.buscarCuenta(op1).misBolsillos)==0:
                    print("El bolsillo no existe")
                    return
                print("1.Descarga completa")
                print("2.Descarga parcial")
                op2 = int(input())
                if op2 < 1 or op2 >2:
                    print("Opción no valida")
                    return
                if op2 == 1:
                    print(cliente.descargarAhorro(cuenta, op1))
                elif op2 == 1:
                    print("Valor a descargar de tu bolsillo")
                    valorDescarga = int(input())
                    print(cliente.descargarAhorro(cuenta, op1, valorDescarga))
                else:
                    print("Opción no valida")