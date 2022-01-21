import numpy as np
import os
import pandas
def k_vecinos():
    dataset = 'validacion_cruzada\\Validacion.csv'
    proDataSet = pandas.read_csv(dataset, header=0)
    DataSetValid = proDataSet.set_index(proDataSet.columns.values[0])
    df = pandas.DataFrame()#tendra las Distancias euclidianas con sus indices
    i=DataSetValid.shape[1]-1
    while(10<i):#DataSet sin las columnas de prueba, entreno, indexpermutado y clase
        DataSetValid = DataSetValid.drop(DataSetValid.columns[i],axis=1)
        i-=1
    i=0
    K=0
    parte=1 #El numero de prueba y entreno a usar
    j=0
    clasePrediccion = " "
    numeroDeIndices=0
    numeroDeAciertos=0
    porcentajeAciertoLocal=[0,0,0,0,0]
    while(K==0):#Este ciclo es para obtener un valor K==3 o 5 o 7 si coloca otro número o letra esto hara que introduzca el valor nuevamente
        try:
            K = int(input("Definir K (3,5,7)"))
        except ValueError:
            print("No es válido")
        if(K==3 or K==5 or K==7):
            break
        elif(K!=3 or K!=5 or K!=7):
            print("Intente nuevamente")
            K=0
    while(i<len(proDataSet["prueba 1"])):#ciclo que se repite la cantidad de filas que hayan en el dataframe
        if(proDataSet.iloc[i]["prueba "+str(parte)]== " "):#este if es para cuando se acaban los valores de una prueba para pasar a otra y resetear variables
            porcentajeAciertoLocal[parte-1]=(numeroDeAciertos*100)/numeroDeIndices#guarda el promedio de aciertos que se obtuvo en una prueba
            parte+=1
            numeroDeIndices=0
            numeroDeAciertos=0
        else:
            numeroDeIndices+=1#para tener cuenta del numero total de filas no nulas en prueba
            while(j<len(proDataSet["prueba 1"])):#ciclo que se repite la cantidad de filas que hayan en el dataframe
                if(proDataSet.iloc[j]["entreno "+str(parte)] not in proDataSet.index):#basicamente ve si el valor de entreno es vacio para agregar datos vacios en la posicion j a la columna resultado e indice de un nuevo df
                    df.at[j,"resultado"] = None
                    df.at[j,"indice"] = None
                    j+=1
                else:#si el valor de entreno no es vacio saca la distancia euclidiana entre el valor de entreno y el valor de prueba
                    indiceEntreno=proDataSet.iloc[j]["entreno "+str(parte)]
                    indicePrueba=proDataSet.iloc[i]["prueba "+str(parte)]
                    DistEucl=np.linalg.norm(DataSetValid.loc[DataSetValid.index[int(indicePrueba)]]-DataSetValid.loc[DataSetValid.index[int(indiceEntreno)]])
                    if(DistEucl<0):#se comprueba si la distancia euclidiana es negativa para volverla positiva y comparar más adelante
                        DistEucl= DistEucl*-1
                    df.at[j,"resultado"] =DistEucl
                    df.at[j,"indice"] = indiceEntreno #se guarda resultado y el indice de entreno en la misma pocision para luego ver que indice entreno tiene menor distancia
                    j+=1
            j=0
            df = df.sort_values("resultado")[:K]#ordena el df de menor a mayor de acuerdo al resultado hasta k valores
            df = df.reset_index(drop=True)
            while(j<K):#ciclo que tiene como funcion tomar el valor de las clases de los indices que menor distancia hayan tenido
                clasePrediccion = clasePrediccion + str(proDataSet.iloc[int(float(df.iloc[j]["indice"]))]["HeartDisease"])
                j+=1
            print("las clases son: "+clasePrediccion)
            if(clasePrediccion.count("1")>=round(K/2)):#se ve si la prediccion con clase de valor 1 es mayor a la mitad de K, siendo asi mayoria
                print("Por mayoria es 1")              #y se comprueba si es que efectivamente la prediccion fue acertada o fallida guardando el numero de aciertos
                if(proDataSet.iloc[int(indicePrueba)]["HeartDisease"]==1):
                    print("la clase es:"+str(proDataSet.iloc[int(indicePrueba)]["HeartDisease"])+", acertó!")
                    numeroDeAciertos+=1
                else:
                    print("la clase es:"+str(proDataSet.iloc[int(indicePrueba)]["HeartDisease"])+", fallo")
            else:#el valor mayoritario es 0 y se ve si acerto o fallo, guardando el numero de aciertos
                print("Por mayoria es 0")
                if(proDataSet.iloc[int(indicePrueba)]["HeartDisease"]==0):
                    print("la clase es:"+str(proDataSet.iloc[int(indicePrueba)]["HeartDisease"])+", acertó!")
                    numeroDeAciertos+=1
                else:
                    print("la clase es:"+str(proDataSet.iloc[int(indicePrueba)]["HeartDisease"])+", fallo")
            print(df)
            j=0
            clasePrediccion = " "
            df = df.iloc[0:0]#se vacia el df 
            print("indice de prueba:"+indicePrueba+". Bloque de prueba:"+str(parte))
        i+=1
    porcentajeAciertoLocal[parte-1]=(numeroDeAciertos*100)/numeroDeIndices#guarda el promedio de aciertos que se obtuvo en el ultimo fold
    print("acierto local:"+str(porcentajeAciertoLocal)+"\nacierto global:"+str(sum(porcentajeAciertoLocal)/len(porcentajeAciertoLocal))+" +/-"+str(np.std(porcentajeAciertoLocal)))
