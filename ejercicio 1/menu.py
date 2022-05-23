from manejador import Manejador
class Menu:
    __options=None

    def __init__(self):
        self.__options=0
    
    def Iniciar(self):
        unManejador=Manejador()
        unManejador.Iniciar()
        while self.__options!='4':
            print('1.Buscar Facultad por codigo')
            print('2.Buscar Carrera por nombre')
            print('3.Eliminar carrera')
            print('4.Salir')
            self.__options=input('ingrese opcion:')

            if self.__options=='1':
                cod=input('ingrese codigo de la Facultad:')
                unManejador.BusquedadeFacultad(cod)
            
            elif self.__options=='2':
                nombre=input('\nIngrese el nombre de la carrera a buscar:')
                unManejador.BusquedadeCarrera(nombre)
            
            elif self.__options=='3':
                nombre=input('\nIngrese el nombre de la carrera a buscar:')
                unManejador.Borrar(nombre)