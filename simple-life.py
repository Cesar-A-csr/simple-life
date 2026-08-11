import random

nombre_jugador = input("Ingresa el nombre de tu personaje: ").strip()
# bucle para que 'nombre_jugador' no sea vacio
while not nombre_jugador:
    nombre_jugador = input("Opción invalida, no puede estar vacío el nombre. Ingresa el nombre de tu personaje: ").strip()

dict_jugador = {
        "nombre": nombre_jugador,
        "dinero": 367,
        "hambre": 0,
        "renta": random.randint(100, 300),
        "salario": random.randint(275, 367)
    }

dict_tiempo = {
        "dia": 1,
        "dias transcurridos": 1,
        "semanas transcurridas": 0,
        "meses trancurridos": 0
    }

while True:

    dict_producto = {
        "manzana": {
            "cantidad": random.randint(2, 8),
            "precio": round(random.uniform(0.25, 0.50), 2),
            "saciedad": 4,
            "tipo": "fruta"
        },
        "racimo de uva": {
            "cantidad": random.randint(1, 10),
            "precio": round(random.uniform(2.50, 5), 2),
            "saciedad": 8.5,
            "tipo": "fruta"
        },
        "zanahoria": {
            "cantidad": random.randint(1, 8),
            "precio": round(random.uniform(0.25, 0.75), 2),
            "saciedad": 5.5,
            "tipo": "verdura"
        },
        "papa": {
            "cantidad": random.randint(4, 10),
            "precio": round(random.uniform(0.75, 1.50), 2),
            "saciedad": 7,
            "tipo": "verdura"
        }
    }
    ls_claves_producto = list(dict_producto.keys())

    print("\n", "#"*20, "Tiempo", "#"*20, "\n")
    for propiedad, valor in list(dict_tiempo.items()):
        print(f"\t{propiedad.capitalize()}: {valor}")
    input("\nPresione Enter tecla para contuinar...")

    print("\n", "#"*20, "Jugador", "#"*20, "\n")
    for propiedad, valor in list(dict_jugador.items()):
        print(f"\t{propiedad.capitalize()}: {valor}")
    input("\nPresione Enter tecla para contuinar...")

    print("\n", "#"*20, "Mercado", "#"*20, "\n")
    for producto, info in dict_producto.items():
        print(f"\t{producto}")
        for propiedad, valor in info.items():
            # mostramos los distintos items (prop: val) de un producto
            print(f"\t\t{propiedad}: {valor}")
    input("\nPresione Enter tecla para contuinar...")

    print("\n", "#"*20, "Compra", "#"*20, "\n")
    print("\t¿Qué deseas comprar?\n")
    while True:
        # Uso de enumerate para numeración automática
        for numeral, clave in enumerate(ls_claves_producto, start=1):
            print(f"\t{numeral}. {clave}")
        # manejos de errores
        try:
            opcion = int(input("\n\tIngresa el número: "))
            # comprobamos que sea un numeral disponible
            if 1 <= opcion <= len(ls_claves_producto):
                indice = opcion - 1
                break
            print(f"\tOpción inválida, debe ser un número entre (1-{len(ls_claves_producto)})\n")
        # manejo de excepcion si el usuario ingresa algo que no es un número
        except ValueError:
            print("\tError: debes ingresar un número\n")

    producto_elegido = ls_claves_producto[indice]           # producto elegido
    dict_datos_producto = dict_producto[producto_elegido]   # diccionario con los dato del producto elegido
    cantidad_disponible = dict_datos_producto['cantidad']   # cantidad del producto elegido
    precio_producto = dict_datos_producto['precio']         # precio del producto elegio
    saciedad_producto = dict_datos_producto['saciedad']     # saciedad del producto elegido

    # bucle para manejo de la cantidad a comprar
    while True: 
        try:
            cantidad_elegida = int(input((f"\tCuanto quieres comprar? ({producto_elegido}): ")))
            # comprabamos que la cantidad no sea <= 0
            if cantidad_elegida <= 0:
                print("\tCantidad invalida, tiene que ser mayor a 0\n")
            # comprobamos que la cantidad ingresada no sea mayor a la cantidad disponible
            elif (cantidad_elegida > cantidad_disponible):
                print(f"\tCantidad invalida, el mercado solo tiene: {cantidad_disponible}\n")
            else:
                break
        except ValueError:
            print("\tError: debes ingresar un número entero\n")

    total_compra = round(cantidad_elegida * precio_producto, 2)
    print(f"\n\tPrecio unitario: ${precio_producto} Cantidad: {cantidad_elegida}")
    print(f"\tTotal: ${total_compra}")
    input("\nPresione Enter tecla para contuinar...")

    if dict_tiempo["dia"] == 1:
        print(f"\n\tHOY ES EL PRIMER DIA DEL MES, SE TE COBRA LA RENTA: ${dict_jugador['renta']}")
        gasto_generado = dict_jugador["renta"] + total_compra
    else:
        gasto_generado = total_compra

    energia_gastada = random.randint(25, 50)
    energia_recuperada = round(saciedad_producto * cantidad_elegida, 2)

    dict_jugador["hambre"] = max(0, dict_jugador["hambre"] + energia_gastada - energia_recuperada)
    dict_jugador["dinero"] = round(dict_jugador["dinero"] - gasto_generado, 2)

    print("\n", "#"*20, "Fin del día", "#"*20, "\n")
    print(f"\tHas gastado: ${gasto_generado}")
    print(f"\tDinero actual: ${dict_jugador['dinero']}")
    print(f"\tEnergía consumida por el día: {energia_gastada}")
    print(f"\tEnergía recuperada por comida: {energia_recuperada}")          
    print(f"\tHambre actual: {dict_jugador['hambre']}")

    # comprobamos que sea un día de 'pago'
    if dict_tiempo["dia"] == 15 or dict_tiempo["dia"] == 30:
        print(f"\n\tHoy no ha sido tan mal día, han pagado, ingresaron: ${dict_jugador['salario']}")
        dict_jugador["dinero"] = round(dict_jugador["dinero"] + dict_jugador["salario"], 2)

    # manejo del fin de mes
    if  dict_tiempo["dia"] == 30:
        dict_tiempo["dia"] = 0 # se resetea a 0, luego aumenta 1
        seguir = input("\t\nHas completado un mes, ¿Quíeres continuar? [s/n] " ).lower().strip()

        if seguir != 's':
            print("\tGracias por tu tiempo, adios")
            break

    input("\nPresione Enter tecla para contuinar...")

    # actualización del dict_tiempo 
    dict_tiempo["dias transcurridos"] += 1 
    dict_tiempo["dia"] += 1
    dict_tiempo["meses trancurridos"] = int(dict_tiempo["dias transcurridos"] // 30)
    dict_tiempo["semanas transcurridas"] = int(dict_tiempo["dias transcurridos"] // 7)

    if dict_jugador["dinero"] <= 0:
        print("\tTe has quedado sin dinero. Bancarrota")
        break
    if dict_jugador["hambre"] >= 100:
        print("\tTu nivel de hambre llegó al 100. Has colapsado")
        break

print("\nFIN DEL JUEGO\n")