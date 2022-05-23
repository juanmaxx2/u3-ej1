class Carrera:
    __Codigo=None
    __Nombre=None
    __Titulo=None
    __Duracion=None
    

    def __init__(self,codigo,nombre,titulo,duracion):
        self.__Codigo=codigo
        self.__Nombre=nombre
        self.__Titulo=titulo
        self.__Duracion=duracion
            
    def getCodigo(self):
        return self.__Codigo
    
    def getNombre(self):
        return self.__Nombre
    
    def getTitulo(self):
        return self.__Titulo
    
    def getDuracion(self):
        return self.__Duracion