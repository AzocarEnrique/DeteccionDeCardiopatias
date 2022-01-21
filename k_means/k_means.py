import pandas                         
import numpy as np                           
import random                                
from funciones import opcion, Desviacion, graficar, acierto
def k_means():
    dataset = 'balance_normalizacion\\ByN.csv'
    DataSet = pandas.read_csv(dataset, header=0)
    DataSet = DataSet.set_index(DataSet.columns.values[0])
    proDataSet = DataSet.iloc[:, :-1]#Para tener un DataSet con la clase incluida y otro con la clase excluida
    nube_1 = []
    nube_2 = []
    nube_1.append(proDataSet.index[random.randint(0, len(proDataSet)-1)])#obtiene el indice del centroide 1
    centroide_1 = proDataSet.loc[nube_1]
    suma_nube_1 = proDataSet.loc[nube_1]
    nube_2.append(proDataSet.index[random.randint(0, len(proDataSet)-1)])#obtiene el indice del supuesto centroide 2
    while(True):
        if(nube_1 == nube_2):#ve si los indices son los mismos para cambiarlos y asignar el centroide 2
            nube_2 = []
            nube_2.append(proDataSet.index[random.randint(0, len(proDataSet)-1)])
        elif(nube_2 != nube_1):
            centroide_2 = proDataSet.loc[nube_2]
            suma_nube_2 = proDataSet.loc[nube_2]
            break
    print(centroide_1)
    print(centroide_2)
    j = 1
    while(True):
        i = 0
        while(i < len(proDataSet)):
            if(proDataSet.index[i] not in nube_1 and proDataSet.index[i] not in nube_2):#Ve si la fila del dataset no es el centroide
                DistEucl_1 = abs(np.linalg.norm(proDataSet.loc[proDataSet.index[i]]-centroide_1))#calcula la distancia euclidiana con su valor absoluto
                DistEucl_2 = abs(np.linalg.norm(proDataSet.loc[proDataSet.index[i]]-centroide_2))
                if(DistEucl_1 <= DistEucl_2):#ve si la distancia es más cercana al centroide 1 que al 2
                    nube_1.append(proDataSet.index[i])#se lleva los indices de los patrones
                    suma_nube_1 = np.add(suma_nube_1, proDataSet.loc[proDataSet.index[i]])#realiza una suma entre los patrones de las nubes
                else:
                    nube_2.append(proDataSet.index[i])#se lleva los indices de los patrones
                    suma_nube_2 = np.add(suma_nube_2, proDataSet.loc[proDataSet.index[i]])#realiza una suma entre los patrones de las nubes
            i += 1
        if(j == 10):#esto es para que el ciclo se recorra 10 veces antes de preguntar
            graficar(proDataSet, nube_1, nube_2, centroide_1, centroide_2)
            print("La cantidad de datos de la nube 1 es: "+str(len(nube_1)))
            print("La cantidad de datos de la nube 1 es: "+str(len(nube_2)))
            j = 1
            print("Quiere calcular nuevos centroides? y=si, n=no:")
            x = opcion("y", "n")#funcion que asegura el input y o n
            if(x == "n"):
                break
        print("\n\n\n\n\n\n\n")
        print(suma_nube_1/len(nube_1))
        print("\n\nDesviacion estandar entre el centroide 1 anterior y el actual:")
        Desviacion(suma_nube_1/len(nube_1), centroide_1)#muestra la desviacion ente el centroide actual y el anterior
        print(suma_nube_2/len(nube_2))
        print("\n\nDesviacion estandar entre el centroide 2 anterior y el actual:")
        Desviacion(suma_nube_2/len(nube_2), centroide_2)#muestra la desviacion ente el centroide actual y el anterior
        centroide_1 = suma_nube_1/len(nube_1)#esto es el promedio de las filas en la nube 1, el nuevo centroide
        centroide_2 = suma_nube_2/len(nube_2)#esto es el promedio de las filas en la nube 2, el nuevo centroide
        nube_1 = []
        nube_2 = []
        suma_nube_1 = np.add(suma_nube_1, -suma_nube_1)#se vacia suma_nube_1
        suma_nube_2 = np.add(suma_nube_2, -suma_nube_2)#se vacia suma_nube_2
        j += 1
    print("que clase tiene la nube 1?")
    suma_nube_1 = int(opcion("1", "0"))#funcion que asegura el input 1 o 0
    print("que clase tiene la nube 2?")
    suma_nube_2 = int(opcion("1", "0"))#funcion que asegura el input 1 o 0
    sumaAciertos = ((acierto(DataSet, suma_nube_1, nube_1)+acierto(DataSet, suma_nube_2, nube_2))*100)/len(DataSet)
    print("\n\n\ncantidad de datos para la nube 1 es de: "+str(len(nube_1))+" y para nube 2 es de: "+str(len(nube_2)))
    print("el porcentaje de acierto en la nube 1 es: "+str(round((acierto(DataSet, suma_nube_1, nube_1)/len(nube_1))*100,2))+"% y de la nube 2 es: "+str(round((acierto(DataSet, suma_nube_2, nube_2)/len(nube_2))*100,2))+"%")
    print("el porcentaje de acierto total es:"+str(round(sumaAciertos,2))+"%")