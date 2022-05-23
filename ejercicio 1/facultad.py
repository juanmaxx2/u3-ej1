from carrera import Carrera
class Facultad:
    __Codigo=None
    __Nombre=None
    __Direccion=None
    __Localidad=None
    __Telefono=None
    __ListaCarrera=[]

    def __init__(self,codigo,nombre,direccion,localidad,telefono,listaCarrera):
        self.__Codigo=codigo
        self.__Nombre=nombre
        self.__Direccion=direccion
        self.__Localidad=localidad
        self.__Telefono=telefono
        for i in range(len(listaCarrera)):
            self.__ListaCarrera.append(Carrera(listaCarrera[i][1],listaCarrera[i][2],listaCarrera[i][3],listaCarrera[i][4]))
    
    def getCodigo(self):
        return self.__Codigo

    def getNombre(self):
        return self.__Nombre

    def getDireccion(self):
        return self.__Direccion
    
    def getLocalidad(self):
        return self.__Localidad

    def getTelefono(self):
        return self.__Telefono
    
    def getCarreraC(self,i):
        return self.__ListaCarrera[i].getCodigo()
    
    def getCarreraN(self,i):
        return self.__ListaCarrera[i].getNombre()
    
    def getCarreraD(self,i):
        return self.__ListaCarrera[i].getDuracion()
    
    def Eliminar(self,i):
        del self.__ListaCarrera[i]
        