import os

CARPETA='contactos/'#Carpeta de Contactos
EXTENSION='.txt'#Extension

#Contactos

class Contacto:
    def __init__(self, nombre, telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()
    #Muestra el Menu de Opciones
    mostrar_menu()
    #Preguntar al usuario que accion realizar
    preguntar= True
    while preguntar:
        opcion= int(input('Seleccione una opcion: \r\n'))

        #Ejecutar las opciones
        if opcion==1:
            agregar_contacto()
            preguntar= False
        elif opcion==2:
            editar_contacto()
            preguntar= False
        elif opcion==3:
            mostrar_contactos()
            preguntar= False
        elif opcion==4:
            buscar_contacto()
            preguntar= False
        elif opcion==5:
            print('BorrarContacto')
            preguntar= False
        else:
            print('Opción no Válida')
def eliminar_contacto():
    nombre = input('Escriba el contacto que quiere eliminar:\r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Eliminado Correctamente')

    except expression as identifier:
        print('No existe ese contacto.')

    app()

def buscar_contacto():
    nombre= input('Escriba el nombre que desea buscar:\r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())

    except IOError:
        print('El archivo no existe')
        print(IOError)

    app()

def mostrar_contactos():
    archivos=os.listdir(CARPETA)

    archivos_txt= [ i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contactos
                print(linea.rstrip())
            #Imprime separador de los contactos
            print('\r\n')

    app()

def editar_contacto():

    nombre_anterior= input('Ingrese el nombre del contacto que desea editar: ')

    # Revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            nombre_contacto = input('Agrega el Nuevo Nombre: ')
            telefono_contacto = input('Agrega el Nuevo Telefono: ')
            categoria_contacto = input('Agrega la Nueva Categoría: ')

            #Instanciamos la clase

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribimos en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Renombramos el archivo

            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar Mensaje de Exito
            print('Contacto Editado Correctamente.\r\n')


    else:
        print('Ese contacto no existe')

    app()

def agregar_contacto():
    print('Escribe los datos del nuevo contacto:')
    nombre_contacto = input('Nombre del Contacto:')

    #Revisar si el archivo existe antes de crearlo

    existe = existe_contacto(nombre_anterior)

    if not existe:


        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            telefono_contacto = input('Agrega el Telefono: ')
            categoria_contacto = input('Agrega la Categoría: ')

            #instanciamos la clase
            contacto= Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #escribimos en el archivo
            archivo.write('Nombre: '+contacto.nombre+'\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            print('Contacto Creado con Exito.\r\n')

    else:
        print('Ese contacto ya existe.')

    #reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione que desea realizar:')
    print('1- Agregar Nuevo Contacto.')
    print('2- Editar Contacto.')
    print('3- Ver Contactos.')
    print('4- Buscar Contacto.')
    print('5- Borrar Contacto.')


def crear_directorio():
    if not os.path.exists('contactos/'):
        #Crear Carpeta
        os.makedirs('contactos/')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
