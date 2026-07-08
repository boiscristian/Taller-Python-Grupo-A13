# TRABAJO FINAL INTEGRADOR - ALGORITMOS Y ESTRUCTURAS DE DATOS 2026
# ESCENARIO 2: SISTEMA DE RESERVAS DE CINE (DATOS REALES CINEMACENTER)

# --- AMBIENTE ---
peli1_nombre = "Minions & Monstruos"
peli2_nombre = "Toy Story 5"
peli3_nombre = "Supergirl"

precio_2d = 13000.0
precio_3d = 14000.0

p1_h1_info = "16:30 (2D)"
p1_h1_formato = "2D"
p1_h1_capacidad = 50
p1_h1_vendidas = 0

p1_h2_info = "18:30 (2D)"
p1_h2_formato = "2D"
p1_h2_capacidad = 50
p1_h2_vendidas = 0

p2_h1_info = "18:00 (2D)"
p2_h1_formato = "2D"
p2_h1_capacidad = 50
p2_h1_vendidas = 0

p2_h2_info = "16:40 (3D)"
p2_h2_formato = "3D"
p2_h2_capacidad = 40
p2_h2_vendidas = 0

p3_h1_info = "21:50 (2D)"
p3_h1_formato = "2D"
p3_h1_capacidad = 60
p3_h1_vendidas = 0

total_entradas_vendidas = 0
total_recaudado = 0.0

ventas_peli1 = 0
ventas_peli2 = 0
ventas_peli3 = 0


# VALIDACION 

def es_opcion_valida(valor, minimo, maximo):
    return minimo <= valor <= maximo


def leer_entero_validado(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if es_opcion_valida(valor, minimo, maximo):
                return valor
            else:
                print("Error: Por favor, ingrese un numero entre", minimo, "y", maximo)
        except ValueError:
            print("Error: Tipo de dato invalido. Debe ser un numero entero.")


# SELECCION Y PROCESAMIENTO

def mostrar_cartelera():
    print("\n--- PELICULAS EN CARTELERA ---")
    print("1.", peli1_nombre)
    print("2.", peli2_nombre)
    print("3.", peli3_nombre)


def mostrar_horarios(peli_idx):
    print("\n--- HORARIOS Y FORMATOS DISPONIBLES ---")
    if peli_idx == 1:
        print("1.", p1_h1_info, "(Disponibles:", p1_h1_capacidad - p1_h1_vendidas, ")")
        print("2.", p1_h2_info, "(Disponibles:", p1_h2_capacidad - p1_h2_vendidas, ")")
    elif peli_idx == 2:
        print("1.", p2_h1_info, "(Disponibles:", p2_h1_capacidad - p2_h1_vendidas, ")")
        print("2.", p2_h2_info, "(Disponibles:", p2_h2_capacidad - p2_h2_vendidas, ")")
    elif peli_idx == 3:
        print("1.", p3_h1_info, "(Disponibles:", p3_h1_capacidad - p3_h1_vendidas, ")")


def verificar_capacidad(peli, horario, cantidad):
    if peli == 1 and horario == 1:
        return cantidad <= (p1_h1_capacidad - p1_h1_vendidas)
    elif peli == 1 and horario == 2:
        return cantidad <= (p1_h2_capacidad - p1_h2_vendidas)
    elif peli == 2 and horario == 1:
        return cantidad <= (p2_h1_capacidad - p2_h1_vendidas)
    elif peli == 2 and horario == 2:
        return cantidad <= (p2_h2_capacidad - p2_h2_vendidas)
    elif peli == 3 and horario == 1:
        return cantidad <= (p3_h1_capacidad - p3_h1_vendidas)
    return False


def calcular_importe_cinemacenter(peli, horario, cantidad):
    if peli == 1 and horario == 1:
        formato_actual = p1_h1_formato
    elif peli == 1 and horario == 2:
        formato_actual = p1_h2_formato
    elif peli == 2 and horario == 1:
        formato_actual = p2_h1_formato
    elif peli == 2 and horario == 2:
        formato_actual = p2_h2_formato
    else:
        formato_actual = p3_h1_formato

    subtotal_acumulado = 0.0

    print("\n--- SELECCION DE TARIFAS INDIVIDUALES ---")
    print("Defina la tarifa correspondiente para cada entrada:")

    for i in range(cantidad):
        print("\nConfigurando entrada", i + 1, "de", cantidad)
        print("1. Entrada General")
        print("2. Promocion Lunes y Martes")
        print("3. Menores de 12 años / Jubilados")
        tipo_tarifa = leer_entero_validado("Seleccione el tipo de tarifa (1-3): ", 1, 3)

        if formato_actual == "2D":
            precio_base = precio_2d
        else:
            precio_base = precio_3d

        if tipo_tarifa == 2:
            precio_ticket = precio_base / 2
        elif tipo_tarifa == 3:
            if formato_actual == "2D":
                precio_ticket = 10000.0
            else:
                precio_ticket = 11000.0
        else:
            precio_ticket = precio_base

        subtotal_acumulado += precio_ticket

    if cantidad >= 4:
        descuento_volumen = 0.15
        print("\nDescuento extra aplicado: 15% por compra de 4 o mas entradas.")
    elif cantidad >= 2:
        descuento_volumen = 0.10
        print("\nDescuento extra aplicado: 10% por compra de 2 o 3 entradas.")
    else:
        descuento_volumen = 0.0

    return subtotal_acumulado - (subtotal_acumulado * descuento_volumen)


# ARCHIVOS

def guardar_reserva_en_archivo(pelicula, horario_info, cantidad, importe):
    with open("historial_ventas.txt", "a") as archivo:
        linea = f"{pelicula},{horario_info},{cantidad},{importe}\n"
        archivo.write(linea)


# LOGICA DEL SISTEMA

def procesar_reserva():
    global p1_h1_vendidas, p1_h2_vendidas, p2_h1_vendidas, p2_h2_vendidas, p3_h1_vendidas
    global total_entradas_vendidas, total_recaudado, ventas_peli1, ventas_peli2, ventas_peli3

    mostrar_cartelera()
    peli = leer_entero_validado("Seleccione el numero de la pelicula (1-3): ", 1, 3)

    max_horario = 2 if (peli == 1 or peli == 2) else 1
    mostrar_horarios(peli)
    horario = leer_entero_validado("Seleccione el numero de horario: ", 1, max_horario)

    capacidad_ok = False
    cantidad = 0
    while not capacidad_ok:
        cantidad = leer_entero_validado("Ingrese cantidad de entradas (1-10): ", 1, 10)
        capacidad_ok = verificar_capacidad(peli, horario, cantidad)
        if not capacidad_ok:
            print("Error: No hay suficientes asientos disponibles. Intente de nuevo.")

    importe_final = calcular_importe_cinemacenter(peli, horario, cantidad)
    print("\nTotal a abonar: $", importe_final)

    confirmar = input("Confirmar operacion? (S/N): ").strip().upper()
    if confirmar == "S":
        total_entradas_vendidas += cantidad
        total_recaudado += importe_final

        if peli == 1:
            ventas_peli1 += cantidad
            if horario == 1:
                p1_h1_vendidas += cantidad
                horario_texto = p1_h1_info
            else:
                p1_h2_vendidas += cantidad
                horario_texto = p1_h2_info
            peli_texto = peli1_nombre
        elif peli == 2:
            ventas_peli2 += cantidad
            if horario == 1:
                p2_h1_vendidas += cantidad
                horario_texto = p2_h1_info
            else:
                p2_h2_vendidas += cantidad
                horario_texto = p2_h2_info
            peli_texto = peli2_nombre
        elif peli == 3:
            ventas_peli3 += cantidad
            p3_h1_vendidas += cantidad
            horario_texto = p3_h1_info
            peli_texto = peli3_nombre

        guardar_reserva_en_archivo(peli_texto, horario_texto, cantidad, importe_final)
        print("Reserva realizada con exito.")
    else:
        print("Operacion cancelada.")


def mostrar_estadisticas():
    if total_entradas_vendidas == 0:
        print("Sin movimientos registrados en la caja.")
        return

    print("\n========= METRICAS DEL CINE =========")
    print("• Total de tickets emitidos:", total_entradas_vendidas)
    print("• Recaudacion total de caja: $", total_recaudado)

    if ventas_peli1 >= ventas_peli2 and ventas_peli1 >= ventas_peli3:
        print("• Pelicula mas vista:", peli1_nombre, "(", ventas_peli1, "entradas)")
    elif ventas_peli2 >= ventas_peli1 and ventas_peli2 >= ventas_peli3:
        print("• Pelicula mas vista:", peli2_nombre, "(", ventas_peli2, "entradas)")
    else:
        print("• Película mas vista:", peli3_nombre, "(", ventas_peli3, "entradas)")
    print("=====================================")


def menu_principal():
    opc = 0
    while opc != 3:
        print("\n--- TERMINAL DE AUTOGESTION ---")
        print("1. Reservar Entradas")
        print("2. Ver Estadisticas (Admin)")
        print("3. Salir")
        print("--------------------------------")
        
        opc = leer_entero_validado("Seleccione una opcion (1-3): ", 1, 3)
        
        if opc == 1:
            procesar_reserva()
        elif opc == 2:
            mostrar_estadisticas()
        elif opc == 3:
            print("\nMuchas gracias por utilizar nuestro sistema.")


if __name__ == "__main__":
    menu_principal()
