
# TRABAJO Laboratorio de Python - ALGORITMOS Y ESTRUCTURAS DE DATOS 2026
# ESCENARIO 2: SISTEMA DE RESERVAS DE CINE (DATOS REALES CINEMACENTER)

# --- AMBIENTE ---
peli1_nombre = "Minions & Monstruos"
peli2_nombre = "Toy Story 5"
peli3_nombre = "Supergirl"

# Precios Base por Formato
precio_2d = 13000.0
precio_3d = 14000.0

# Funciones y Horarios Disponibles
# Pelicula 1: Minions & Monstruos (Solo 2D)
p1_h1_info = "16:30 (2D)"
p1_h1_formato = "2D"
p1_h1_capacidad = 50
p1_h1_vendidas = 0

p1_h2_info = "18:30 (2D)"
p1_h2_formato = "2D"
p1_h2_capacidad = 50
p1_h2_vendidas = 0

# Pelicula 2: Toy Story 5 (Tiene una funcion 2D y una 3D)
p2_h1_info = "18:00 (2D)"
p2_h1_formato = "2D"
p2_h1_capacidad = 50
p2_h1_vendidas = 0

p2_h2_info = "16:40 (3D)"
p2_h2_formato = "3D"
p2_h2_capacidad = 40
p2_h2_vendidas = 0

# Pelicula 3: Supergirl (Solo 2D)
p3_h1_info = "21:50 (2D)"
p3_h1_formato = "2D"
p3_h1_capacidad = 60
p3_h1_vendidas = 0

# Variables globales para estadisticas
total_entradas_vendidas = 0
total_recaudado = 0.0

ventas_peli1 = 0
ventas_peli2 = 0
ventas_peli3 = 0


# --- PROGRAMA PRINCIPAL ---

def menu_principal():
    opc = 0
    while opc != 3:
        print("\n--- TERMINAL DE AUTOGESTION ---")
        print("1. Reservar Entradas (En desarrollo)")
        print("2. Ver Estadisticas (En desarrollo)")
        print("3. Salir")
        print("--------------------------------")
        
        opc = int(input("Seleccione una opcion (1-3): "))
        
        if opc < 1 or opc > 3:
            print("Error: Opcion invalida. Ingrese un numero entre 1 y 3.")
        elif opc == 1:
            print("\n[En desarrollo...]")
        elif opc == 2:
            print("\n[En desarrollo...]")
        elif opc == 3:
            print("\nMuchas gracias por utilizar nuestro sistema.")


if __name__ == "__main__":
    menu_principal()
