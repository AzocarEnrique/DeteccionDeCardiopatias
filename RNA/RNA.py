import pandas  
import os                       
import numpy as np   
from funciones import pesosrand, sumatoriaybias, sigmoid, opcion, relu 
def RNA():                            
    dataset = 'validacion_cruzada\\Validacion.csv'
    DataSet = pandas.read_csv(dataset, header=0)
    DataSet = DataSet.set_index(DataSet.columns.values[0])
    proDataSet = DataSet#para tener un df con clases y otro sin estas
    salida = pandas.DataFrame()#df que guardara las clases verdaderas, las predecidas y el error cuadratico medio
    i = DataSet.shape[1]-1
    while(10 < i):#DataSet sin las columnas de prueba, entreno, indexpermutado y clase
        proDataSet = proDataSet.drop(proDataSet.columns[i], axis=1)
        i -= 1
    i = 0
    j = 0
    pesos1 = pesosrand(len(proDataSet.loc[0]), 2)#pesos de la conexion entre nodos de entrada con los nodos ocultos
    pesos2 = pesosrand(2, 1)#pesos de la conexion de nodos ocultos con la salida
    BiasOculto = [1, 1]
    BiasSalida = [1]
    parte = 1#variable que tiene el numero de fold utilizado en el momento
    print("Seleccione 1 para usar la funcion de activacion sigmoide y 2 para la funcion de activacion rampa: ")
    x= opcion("1","2")
    while(parte<6):
        if(DataSet.iloc[i]["entreno "+str(parte)] not in DataSet.index):#Permite guardar el ECM de un fold, reiniciar variables y cambiar de fold
            i += 1
        else:
            salida.at[j, "clase real fold "+str(parte)] = DataSet.iloc[int(DataSet.iloc[i]["entreno "+str(parte)])]["HeartDisease"]#guarda la clase real en el df de salida 
            if(x == "1"):#usa la funcion de activacion sigmoide
                nodo_oculto1 = sigmoid(sumatoriaybias(list(proDataSet.loc[int(DataSet.iloc[i]["entreno "+str(parte)])]), pesos1[0], BiasOculto[0]))#realiza la sumatoria de variables multiplicadas a sus pesos respectivos y la suma del bias
                nodo_oculto2 = sigmoid(sumatoriaybias(list(proDataSet.loc[int(DataSet.iloc[i]["entreno "+str(parte)])]), pesos1[1], BiasOculto[1]))
                salida.at[j, "valor salida fold "+str(parte)] = round(sigmoid(sumatoriaybias(list([nodo_oculto1, nodo_oculto2]), pesos2[0], BiasSalida[0])), 2)#guarda la prediccion en el df de salida
            elif(x == "2"):#usa la funcion de activacion relu
                nodo_oculto1 = relu(sumatoriaybias(list(proDataSet.loc[int(DataSet.iloc[i]["entreno "+str(parte)])]), pesos1[0], BiasOculto[0]))#realiza la sumatoria de variables multiplicadas a sus pesos respectivos y la suma del bias
                nodo_oculto2 = relu(sumatoriaybias(list(proDataSet.loc[int(DataSet.iloc[i]["entreno "+str(parte)])]), pesos1[1], BiasOculto[1]))
                salida.at[j, "valor salida fold "+str(parte)] = round(relu(sumatoriaybias(list([nodo_oculto1, nodo_oculto2]), pesos2[0], BiasSalida[0])), 2)#guarda la prediccion en el df de salida
            i += 1
            j += 1
        if(i == len(DataSet)):
            i = 0
            salida.at[j, "valor salida fold "+str(parte)] = round(np.square(np.subtract(salida.iloc[:-1, (parte-1)*2],salida.iloc[:-1, (parte*2)-1])).mean(), 3)
            salida["clase real fold "+str(parte)] = salida["clase real fold "+str(parte)].astype(str)#Para pasar las columnas de int a string
            salida["valor salida fold "+str(parte)] = salida["valor salida fold "+str(parte)].astype(str)
            salida.at[j, "clase real fold "+str(parte)] = "ECM"
            parte += 1
            j = 0
            pesos1 = pesosrand(len(proDataSet.loc[0]), 2)#pesos de la conexion entre nodos de entrada con los nodos ocultos
            pesos2 = pesosrand(2, 1)#pesos de la conexion de nodos ocultos con la salida
    ######## Se guarda el ultimo ECM del ultimo fold y se exporta el df salida a csv con el nombre de RNA ##########################
    path = 'RNA\\'
    salida.to_csv(os.path.join(path,'RNA.csv'))