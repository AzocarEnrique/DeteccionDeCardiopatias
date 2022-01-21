import random 
import numpy as np  
import math
from matplotlib import pyplot##### ¡Importante! Se necesita tener instalada la libreria matplotlib para que funcione
def pesosrand(dim1, dim2):#devuelve una matriz con numeros aleatorios del 0.01 al 0.99
    pesos=np.zeros((dim2, dim1))
    j=0
    while(j<dim2):
        i=0
        while(i<dim1):
            pesos[j][i]=round((random.randint(1, 99))*0.01, 2)
            i+=1
        j+=1
    return pesos

def sumatoriaybias(variables, pesos, bias):#realiza la sumatoria de las variables por sus pesos respectivos y al final suma el bias
    i=0
    sumatoria = 0
    while(i<len(variables)):
        sumatoria=sumatoria+(variables[i]*pesos[i])
        i+=1
    return sumatoria+bias

def sigmoid(x):#funcion sigmoide
    sig = 1 / (1 + math.exp(-x))
    return sig

def opcion(y, n):#para obtener solo el valor necesario
    while(True):
        x = input()
        if(x == y or x == n):
            break
        else:
            print("selección no valida, intente nuevamente\n")
    return x
def relu(x):#funcion relu
    return max(0.0, x)


def Desviacion(centroideAnterior, centroideActual):#muestra la desviacion estandar que existe entre el centroide actual y el anterior
    i= 0
    suma= 0
    while(i<len(list(centroideActual))):
        paresCentroides = [centroideAnterior.iloc[0][i], centroideActual.iloc[0][i]]
        suma = suma + np.std(paresCentroides)
        i += 1
    print(suma/len(list(centroideActual)))


def graficar(df, nube1, nube2, centroide1, centroide2):#muestra una grafica de las nubes junto con los centroides
    nube1df = df.iloc[nube1]
    nube2df = df.iloc[nube2]
    pyplot.ion()
    pyplot.plot(nube1df.iloc[:, 0], nube1df.iloc[:, 7], 'ro', nube2df.iloc[:, 0], nube2df.iloc[:, 7], 'bo'
                , centroide1.iloc[:, 0], centroide1.iloc[:, 7], 'ms', centroide2.iloc[:, 0], centroide2.iloc[:, 7], 'gs')
    pyplot.xlabel("Edad")
    pyplot.ylabel("ritmo cardiaco")


def acierto(df, clase, nube):
    nube = df.iloc[nube]
    nube = nube.reset_index(drop=True)
    nube = nube.drop(nube[nube['HeartDisease']!=clase].index)
    return len(nube)