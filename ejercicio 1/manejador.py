from facultad import Facultad
from carrera import Carrera
import csv
class Manejador:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def Iniciar(self):
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo, delimiter=',')
        fila=next(reader)
        bandera=True
        while bandera:
            listaCarrera=[]
            filaCarrera=next(reader)
            while bandera and fila[0]==filaCarrera[0]:
                listaCarrera.append(filaCarrera)
                try:
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False
            UnaFacultad = Facultad(fila[0], fila[1], fila[2], fila[3],fila[4], listaCarrera)
            self.__lista.append(UnaFacultad)        
            fila=filaCarrera
        archivo.close()
        
    def BusquedadeFacultad(self,cod):
        i=0
        j=0
        while cod!=self.__lista[i].getCodigo():
            i+=1
        if self.__lista[i].getCodigo()==cod:
            print ('\nPara el codigo {} de la facultad {}, las carreras y su duracion son:'.format(str(self.__lista[i-2].getCodigo()),str(self.__lista[i-2].getNombre())))
            while j<int(self.__lista[i-2].getCarreraC(j)):
                print('Carrera:{}, Duracion:{}'.format(str(self.__lista[i-2].getCarreraN(j)),str(self.__lista[i-2].getCarreraD(j))))
                j+=1

    def BusquedadeCarrera(self,nombre):
        i=0
        j=0
        while nombre != self.__lista[i].getCarreraN(j):
            j+=1
        print ('\nNombre de la facultad es {}, localidad de la facultad es {}, la carrera es {} y el codigo es {}'.format(self.__lista[i].getNombre(),self.__lista[i].getLocalidad(),self.__lista[i].getCarreraN(j),self.__lista[i].getCarreraC(j)))
    
    def __dell__(self):
        self.__lista.get