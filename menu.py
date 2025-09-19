
import libro

# FASE 1: Carga inicial de libros desde archivo
libros = libro.cargar_libros()

# FASE 2: Bucle principal del menú
while True:
    print("\n===== MENÚ BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Mostrar todos los libros")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    # FASE 3: Procesamiento de opciones del menú
    if opcion == "1":
        libro.registrar_libro(libros)
        seguir = input("¿Desea continuar? (Si / No): ")
        if seguir.lower() == "no":
            continue

    elif opcion == "2":
        libro.buscar_libro(libros)
        seguir = input("¿Desea continuar? (Si / No): ")
        if seguir.lower() == "no":
            continue

    elif opcion == "3":
        libro.mostrar_libros(libros)

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
