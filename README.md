# Laboratorio de Python: Sistema de Reservas de Cine
**Asignatura:** Algoritmos y Estructuras de Datos  
**Carrera:** Ingeniería en Sistemas de Información  
**Institución:** Universidad Tecnológica Nacional – Facultad Regional Resistencia (UTN FRRe)  
**Ciclo Lectivo:** 2026  

---

## Integrantes del Grupo - Comisión K1.1
* **Bois**, Cristian Gabriel
* **Comisso Bentz**, Matias Gabriel
* **Ferreyra**, Valentino
* **López Arguello**, Ignacio Nahuel
* **Medina Duran Cantón**, Jose Ignacio

---

## Presentación del Proyecto
Este sistema automatiza el proceso de venta de entradas y control de capacidad para un complejo de cine, adaptando las reglas de negocio a la cartelera y tarifas reales de Cinemacenter Resistencia.

---

## Estructura del Repositorio

* `/Codigo_Fuente`: Contiene el código ejecutable principal en Python (`sistema_cine.py`).
* `/Guia_Orientativa`: Contiene el pseudocódigo inicial desarrollado por el equipo como base lógica de orientación antes de iniciar la programación nativa.

---

## Estado Actual del Desarrollo

El proyecto se encuentra en etapa de construcción colaborativa y progresiva:

* **Ambiente Inicial Configurado:** Declaración estática de variables independientes para el control de capacidad de salas (formatos 2D y 3D), asignación de precios base de la cartelera real de Cinemacenter y contadores globales para la auditoría de caja.
* **Interfaz de Consola Funcional:** Implementación del menú principal mediante un bucle de control condicional (`while`), permitiendo la navegación interactiva y el cierre limpio del sistema (Opción 3).
* **Próximas Integraciones (En desarrollo):** Incorporación de los módulos de validación de entradas por teclado, procesamiento de reservas con quitas promocionales y generación de reportes estadísticos de máximos.
* **Incorporación de dos nuevas funciones (En desarrollo):** Se incorporaron las funciones "reservar_entradas" y "ver_estadisticas" las cuales cuentan con una estructura básica de como serán con la opción de ser modificadas en caso de ser necesario.
* **Integración Completa del Sistema:** El menú principal ahora ejecuta correctamente las funciones de reserva y estadísticas, quedando totalmente conectado (en la versión anterior estas funciones existían pero no estaban vinculadas al menú).
* **Validación de Entradas por Teclado:** Incorporación de las funciones `es_opcion_valida()` y `leer_entero_validado()`, que controlan los rangos permitidos y capturan errores de tipo de dato (`ValueError`), evitando que el sistema se interrumpa ante datos inválidos.
* **Modularización del Código:** Separación de la lógica en funciones específicas (`mostrar_cartelera`, `mostrar_horarios`, `verificar_capacidad`, `calcular_importe_cinemacenter`, `procesar_reserva`, `mostrar_estadisticas`) para mayor claridad y mantenimiento.
* **Reserva Funcional para las 3 Películas:** Se completó la lógica de reserva para Toy Story 5 y Supergirl (antes solo disponible para Minions & Monstruos), con control de capacidad por función.
* **Sistema de Tarifas y Descuentos:** Se agregó selección de tipo de tarifa por entrada (General, Promoción Lunes y Martes, Menores de 12 años/Jubilados) y descuento por volumen de compra (10% en 2-3 entradas, 15% en 4 o más).
* **Confirmación de Operación:** Se incorporó un paso de confirmación (S/N) antes de registrar la venta y actualizar la caja.
