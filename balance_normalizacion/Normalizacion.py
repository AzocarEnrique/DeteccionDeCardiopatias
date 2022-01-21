import os
from numpy import empty, float64, int64, integer
from numpy.core.fromnumeric import prod
import pandas
def Normalizacion(proDataSet):
    aux=0
    indexPalabras = []
    palabras = []
    x=0
    while(True): 
        if(aux<len(proDataSet.columns)):##por la normalizacion que hace que el aux se pase del numero de columnas
            if(x==len(proDataSet[proDataSet.dtypes.index[aux]])):##x==numero de filas
                aux+=1
                x=0
                media = float(sum(proDataSet[proDataSet.dtypes.index[aux-1]]))/float(len(proDataSet[proDataSet.dtypes.index[aux-1]]))
                desvStd = float(proDataSet[proDataSet.dtypes.index[aux-1]].std(axis=0))
        elif(aux==len(proDataSet.columns) and x== len(proDataSet[proDataSet.dtypes.index[aux-1]])):
            aux+=1
            x=0
        if(aux==len(proDataSet.columns)):##aux==numero de columnas
            break
        if(aux<len(proDataSet.columns)):
            if(type(proDataSet.iloc[x][aux]) != int64 and type(proDataSet.iloc[x][aux]) != float and type(proDataSet.iloc[x][aux]) != float64 and proDataSet.iloc[x][aux] not in palabras):##se fija que la columna no sea numerica
                palabras.append(proDataSet.iloc[x][aux])
                ultimaPalabra = palabras.pop()
                while True: 
                    try:
                        num = float(input("Que número desea asignarle a "+ultimaPalabra+" de "+proDataSet.dtypes.index[aux]+"?:"))
                        break
                    except ValueError:
                        print("No es válido")
                indexPalabras.append([proDataSet.dtypes.index[aux],ultimaPalabra,num])##crea una lista con la categoria, el valor cat y el valor numerico
                proDataSet[proDataSet.dtypes.index[aux]].replace({ultimaPalabra:float(num)}, inplace= True)##reemplaza la palabra encontrada por un numero en toda la columna
        if(aux>0):##Esto normalizara a todas las columnas del dataframe
            proDataSet[proDataSet.dtypes.index[aux-1]] = proDataSet[proDataSet.dtypes.index[aux-1]].astype(float)##cambia el valor de la columna a flotante
            normalizado = (float(proDataSet.iloc[x][aux-1])-media)/desvStd ##dato normalizado
            proDataSet.at[x,proDataSet.dtypes.index[aux-1]]=normalizado ##reemplaza el valor de la celda por el normalizado
        x+=1
    print(proDataSet.head)
    id= pandas.DataFrame(indexPalabras, columns= ['categoria','valor_categorico','valor_numerico'])
    path = 'balance_normalizacion\\'
    id.to_csv(os.path.join(path,'lista.csv'))
    x=0
    while(x<len(proDataSet.columns)-1):
        media =float(sum(proDataSet[proDataSet.dtypes.index[x]]))/float(len(proDataSet[proDataSet.dtypes.index[x]]))
        desvStd = float(proDataSet[proDataSet.dtypes.index[x]].std(axis=0))
        print("\nLa media de "+proDataSet.dtypes.index[x]+" es: "+str(media)+" y su desviacion estandar es: "+str(desvStd))
        ######Comprobacion de que la media aproximada es 0 y la desviacion es 1
        if(round(media)!=0):
            print("\nLa media de "+proDataSet.dtypes.index[x]+" es distinta de 0")
            return 1
        if(round(desvStd)!=1):
            print("\nLa esviacion estandar de "+proDataSet.dtypes.index[x]+" es distinta de 1")
            return 1
        x+=1
    return proDataSet