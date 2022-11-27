from main import *
class UIPago:
    def Pagar(cliente):
        print(
                """
                        Seleccione el tipo de pago que desea realizar
                        1. Pagar prestamo
                        2. Pagar multa""")
        opcionPagos=int(input())
        print("Ingresa el ID de la cuenta que deseas aplicar el prestamo")
        Main.traerCuentas()
        opcion = int(input()) #variable que trae la cuenta
        if (opcionPagos == 1):
                if (len(((Cliente.buscarCuenta(opcion)).getPrestamos())) == 0) :
                    print("Usted no cuenta con prestamos actualmente")
                    return
                
                print("Prestamos Actualmente activos: ")
                Main.traerPrestamos(opcion)
                print("elija el ID del prestamo que desea pagar")
                numeroDePrestamo=int(input()) #id del prestamo
                print("""
                        1. Pago parcial
                        2. Pago completo""")

                pago = int(input())

                if (pago == 1) :
                    print("cuantas cuotas desea pagar?")
                    cuotas = int(input()) #numero de cuotas
                    print("Valor de la transaccion: ")
                    print((Cliente.buscarPrestamo(opcion,numeroDePrestamo)).getValorCuota()*cuotas )
                    print("""
                            Desea realizar el pago?
                            1. Si
                            2.No""")
                    caso = int(input())
                    if (caso == 1) :
                        #cuenta, prestamo, cuota
                        print(cliente.hacerPagoPrestamo(opcion,numeroDePrestamo,cuotas))
                          
                elif (pago == 2) :
                    print("Valor de la transaccion: ")
                    print( Cliente.buscarPrestamo(opcion,numeroDePrestamo).getValorPrestamo()* ((int)(1+Cliente.buscarPrestamo(opcion,numeroDePrestamo).getInteres())))
                    print("""
                                Desea realizar el pago?
                                1. Si
                                2.No""")
                    caso = int(input())
                    if (caso == 1) :
                    # cuenta, prestamo
                        print(cliente.hacerPagoPrestamo(opcion,numeroDePrestamo))
                          
        elif (opcionPagos == 2):
            if (((len(Cliente.buscarCuenta(opcion)).getMultas())) == 0) :
                print("Usted no cuenta con multas actualmente")
                return
                
            print("Multas Actualmente activos: ")
            Main.traerMultas(opcion)

            print("Elija el ID de la multa que desea pagar")
            numeroDeMulta=int(input()) #

            print("""
                    1. Pago parcial
                    2. Pago completo""")
            pago = int(input())

            if (pago == 1) :
                
                print("Ingrese el valor de la transaccion")
                valorM = int(input())
                print(cliente.hacerPagoMulta(opcion,numeroDeMulta,valorM))
                    
            if (pago == 2) :
                print("Valor de la transaccion: ")
                print( Cliente.buscarMulta(opcion,numeroDeMulta).getMonto())
                print("""
                        Desea realizar el pago?
                        1. Si
                        2.No""")
                caso = int(input())
                if (caso == 1) :
                    mensaje =cliente.hacerPagoMulta(opcion,numeroDeMulta)
                    print(mensaje)
                        
                    
                
            
        
    

