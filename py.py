#BIBLIOTECA VIRTUAL

sesiones = ['maria','jose','marcelo']
agendaLibros = {'harry potter' : {'Nombre': 'harry potter', 'Autor': 'jose', 'Generos': 'fantasia'}, 'merlin' : {'Nombre': 'merlin', 'Autor': 'maria', 'Generos': 'fantasia'}}

def biblioteca():
    print('\n+---+---+---+---+---+---+---+---+---+---+\n| B | i | b | l | i | o | t | e | c | a |\n+---+---+---+---+---+---+---+---+---+---+\n')
    print('------------------------------------------')
    print('Opcion 1: Buscar Libro')
    print('Opcion 2: Agregar Libro')
    print('Opcion 3: Eliminar Libro')
    print('Opcion 4: Catalogo')
    print('Opcion 5: Agregar Reseña')
    print('Opcion 6: Puntuar Libro')
    print('Escribir cualquier otra opcion, cierra el programa.')
    opcion = int(input ('Elegir Opcion: '))
    print('------------------------------------------')
    opciones(opcion)

def opciones(x):
    if x == 1:
        buscarlibro()
    
    elif x == 2:
        agregarlibro ()

    elif x == 3:
       eliminarLibro(agendaLibros)

    elif x == 4:
        mostrarAgenda(agendaLibros)

def buscarlibro ():
    print ('1: Buscar por autor')
    print ('2: Buscar por nombre')
    print ('3: Buscar por genero')
    eleccion = int (input ('Elija una opcion: '))

    if eleccion == 1:  
        nombreautor = input ('Introducir nombre del autor: ')
        for i in agendaLibros:
            for j in agendaLibros[i].values():
                if nombreautor in j:
                   mostrarAgenda(i)
                else:
                    print('Autor no registrado')
    elif eleccion == 2:  
        nombre = input ('Introducir nombre del libro: ')
        for i in agendaLibros:
            for j in agendaLibros[i].values():
                if nombre in j:
                   mostrarAgenda(i)
                else:
                    print('Libro no registrado')
    elif eleccion == 3:  
        genero = input ('Introducir el genero: ')
        for i in agendaLibros:
            for j in agendaLibros[i].values():
                if genero in j:
                   mostrarAgenda(i)
                else:
                    print('Autor no registrado')
    
def agregarlibro ():
    nombreLibro = input ('Nombre del libro: ')
    autor = input ('Autor/es del libro: ')
    generos = input ('Genero/s del libro (si es nas de uno separarlo con ","): ')  

    if agendaLibros.get(nombreLibro) == None:
        agendaLibros[nombreLibro] = {'Nombre': nombreLibro, 'Autor': autor, 'Generos': generos}  
    else:
        print('El libro ya esta registrado')

def mostrarAgenda (x):
    for i in x:
        for j,k in x[i].items():
            print(j, ':', k)
        print('')
    input()    

def eliminarLibro(x):
    libroBuscado = input('Ingrese el nombre del libro que desea eliminar: ')
    for i in x:
        if i == libroBuscado:
            x.pop(i)
            break
    mostrarAgenda()
  
def registro():
    usuario = input('Ingrese su nombre de usuario: ')
    sesiones.append(usuario)
                
def listaUsuarios():
    for i in sesiones:
        print(i)

def eliminarUsuario():
    usuario = input('\nQue usuario desea eliminar? ')
    for i in sesiones:
        if i == usuario:
            sesiones.remove(usuario)
    
  
while True:
               
    opc = int(input(('\n1) Ir a la biblioteca\n2) Registrarse\n3) Ver que usuarios existen\n4) Eliminar su usuario\n5) Salir\n\topcion? ')))
    if opc == 1:
        biblioteca()
    elif opc == 2:
       registro()
    elif opc == 3:
        listaUsuarios()
    elif opc == 4:
        eliminarUsuario()
    elif opc == 5:
        break
        



