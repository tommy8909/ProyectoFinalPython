#BIBLIOTECA VIRTUAL
""" agregar libro, eliminar libro, caracteristicas del libro, sucursales del libro, mostrar todos los libros,
busqueda de libros (busqueda por autor), menu, un inicio de sesion, diferencia de libros para cada usuario, libros reservados para cada uno, 
filtro por genero, agregar reseñas de libros, puntuar libros
"""
agendalibros = {'hola'}

def buscarlibro (opcion):
    print ('1: Buscar por autor')
    print ('2: Buscar por nombre')
    print ('3: Buscar por genero')
    eleccion = int (input ('Elija una opcion:'))

    if eleccion == 1:  
        nombreautor = input ('Introducir nombre del autor:')
        for i in agendalibros.keys():
            if nombreautor in i:
                print (agendalibros[i])
            else:
                print('autor no registrado')


    
def agregarlibro (opcion):
    nombrelibro = input ('Nombre del libro:')
    autor = input ('Autor/es del libro:')
    generos = input ('Genero/s del libro (si es nas de uno separarlo con ","):')    

    if agendalibros.get(nombrelibro) == None:
        agendalibros[nombrelibro] = {'Nombre': nombrelibro, 'Autor': autor, 'Generos': generos}
    else:
        print('El libro ya esta registrado')

def mostraragenda (opcion):
    for i in agendalibros:
        for j,k in agendalibros[i].items():
            print(j, ':', k)



while True:

    
    print('------------------------------------------')
    print('Opcion 1: Buscar Libro')
    print('Opcion 2: Agregar Libro')
    print('Opcion 3: Eliminar Libro')
    print('Opcion 4: Mostrar Lista de Libros')
    print('Opcion 5: Agregar Reseña')
    print('Opcion 6: Puntuar Libro')
    print('Opcion 7: Salir')
    opcion = int(input ('Elegir Opcion:'))
    print('------------------------------------------')


    if opcion == 1:
        buscarlibro(opcion)
    
    elif opcion == 2:
        agregarlibro (opcion)
    
    elif opcion == 4:
        mostraragenda(opcion)


    elif opcion == 7:
        break

    

