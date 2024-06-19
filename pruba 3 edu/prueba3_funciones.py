
TipoPedido=["pequeño", "mediano", "grande"]
SECTOR = ["centro", "norte", "sur"]

def Registrar_pedido(PaquExpress):
    nombre = input("Escriba el nombre y apellido del cliente: ")
    direccion = input("Escriba la direccion del cliente: ")
    sector = input("Escriba el sector del cliente (centro/norte/sur): ").lower()
    while sector not in SECTOR:
        print("Ingese un sector valido..")
        sector = input("Escriba el sector del cliente: ").lower()
    cantidadpedido = int(input("Ingrese cuantos pedidos quiere: "))
    detallepedido = []
    for pedidos in range(cantidadpedido):
        paquete = input("ingrese el tamaño del pedido que quiera (Pequeño/Mediano/grande):  ").lower()
        detallepedido.append(paquete)
    
    PaquExpress.append({
        "Nombre":nombre,
        "Dirección":direccion,
        "Sector":sector,
        "Cantidadpedido": cantidadpedido,
        "DetallePedido":detallepedido
        
    })

def Listar_pedidos(PaquExpress):
    for pedidos in PaquExpress:
        print(pedidos)

def Imprimir_ruta(PaquExpress):
    sector = input("Ingrese el sector del pedido que desee ver: ")
    if sector == SECTOR:
        sectores = PaquExpress

    with open(f"planilla_{sector}.txt","w") as archivo:
        for sectores in PaquExpress:
            archivo.write(f"Nombre y apellido del cliente {"Nombre"}\n")
            archivo.write(f"Dirección del cliente {"Dirección"}\n")
            archivo.write(f"Sector del envio {"Sector"}\n")
            archivo.write(f"Cantidad de pedidos {"Cantidadpedido"}\n")
            archivo.write(f"Detalles del pedido {"DetallePedido"}\n\n")