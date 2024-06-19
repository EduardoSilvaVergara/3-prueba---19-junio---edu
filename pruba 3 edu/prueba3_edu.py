import prueba3_funciones as pf

PaquExpress =[]
while True:
    print("******************************")
    print("** Bienvenido a PaquExpress **")
    print("******************************")
    print("1. Registrar pedido")
    print("2. Listar los todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opc=int(input("Escoga una de las sieguientes opciones: "))

    if opc==1:
        pf.Registrar_pedido(PaquExpress)
    elif opc==2:
        pf.Listar_pedidos(PaquExpress)
    elif opc==3:
        pf.Imprimir_ruta(PaquExpress)
    elif opc==4:
        print("Hasta luego...")
        break
    else:
        print("Error, escoga una de las opciones")
