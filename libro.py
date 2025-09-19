
class Libro:
    """
    Clase que representa un libro con sus atributos básicos
    """
    titulo = ""
    autor = ""
    genero = ""
    anio = ""
    paginas = ""

def guardar_libros(libros, archivo="biblioteca.txt"):
    """
    Guarda la lista de libros en un archivo de texto
    Formato: titulo;autor;genero;año;paginas
    """
    with open(archivo, "w") as f:
        for libro in libros:
            f.write(f"{libro.titulo};{libro.autor};{libro.genero};{libro.anio};{libro.paginas}\n")

def cargar_libros(archivo="biblioteca.txt"):
    """
    Carga la lista de libros desde un archivo de texto
    Retorna una lista de objetos Libro
    """
    libros = []
    try:
        with open(archivo, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    datos = linea.split(";")
                    if len(datos) == 5:  # Validar que tenga todos los campos
                        l = Libro()
                        l.titulo = datos[0]
                        l.autor = datos[1]
                        l.genero = datos[2]
                        l.anio = datos[3]
                        l.paginas = datos[4]
                        libros.append(l)
    except FileNotFoundError:
        # Si el archivo no existe, retorna lista vacía
        pass
    return libros

def registrar_libro(libros):
    """
    Registra un nuevo libro solicitando datos al usuario
    y lo agrega a la lista de libros
    """
    l = Libro()
    l.titulo = input("Titulo: ")
    l.autor = input("Autor: ")
    l.genero = input("Genero: ")
    l.anio = input("Año de publicacion: ")
    l.paginas = input("Número de paginas: ")
    libros.append(l)
    guardar_libros(libros)  # Guarda inmediatamente en archivo
    print("Libro registrado con éxito.")

def buscar_libro(libros):
    """
    Busca un libro por título (búsqueda case-insensitive)
    """
    buscar = input("Ingrese el titulo del libro: ")
    encontrado = False
    for l in libros:
        if l.titulo.lower() == buscar.lower():
            print("Encontrado:", l.titulo, "-", l.autor, "-", l.anio)
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado.")

def mostrar_libros(libros):
    """
    Muestra todos los libros registrados en formato lista
    """
    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        print("Lista de libros:")
        for l in libros:
            print(l.titulo, "|", l.autor, "|", l.anio)