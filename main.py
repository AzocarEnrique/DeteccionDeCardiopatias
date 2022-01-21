import os
import pandas
from balance_normalizacion.balance import balance
from balance_normalizacion.ElimNull import ElimNull
from balance_normalizacion.Normalizacion import Normalizacion
from validacion_cruzada.Validacion import validacion
from KNN.k_vecinos import k_vecinos
from RNA.RNA import RNA
from k_means.k_means import k_means
dataset = 'heart.csv'
proDataSet = pandas.read_csv(dataset, header=0)

proDataSet = ElimNull(proDataSet)##Eliminacion de datos nulos
print(proDataSet.head)  

proDataSet = balance(proDataSet)##balanceo
print(proDataSet)

proDataSet = Normalizacion(proDataSet)##Normalizacion, transformacion de datos categoricos a numericos y comprobacion de la normalizacion
print(proDataSet)
path = 'balance_normalizacion\\'
proDataSet.to_csv(os.path.join(path,'ByN.csv'))

path = 'balance_normalizacion\\'
x = 1
while(x==1):# menu que permite seleccionar entre algorimos supervisados y no supervisados
    x=int(input("1 para aplicar algoritmos supervisados (KNN, RNA)\n2 para aplicar algoritmos no supervisados (K-means)\n0 para salir: "))
    if(x==1):
        print("entro a 1")
        validacion()
        x=int(input("1 para KNN\n2 para RNA: "))
        if(x==1):
            k_vecinos()
        elif(x==2):
            RNA()
            x=1
        else:
            print("opción no valida")
            x=1
    elif(x==2):
        k_means()
        x=1
    elif(x==0):
        break
    else:
        print("opcion no valida")
        x=1
