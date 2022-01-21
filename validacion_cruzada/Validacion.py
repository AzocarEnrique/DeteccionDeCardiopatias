import pandas
import os
def validacion():
    dataset = 'balance_normalizacion\\ByN.csv'
    proDataSet = pandas.read_csv(dataset, header=0)
    permutar = proDataSet.sample(frac= 1).reset_index(drop = True) #se permutan los indices y se genera uno nuevo para mantener el orden
    IndicePermutado = permutar[permutar.columns.values[0]]
    proDataSet = proDataSet.set_index(proDataSet.columns.values[0])
    proDataSet["indice permutado"] = IndicePermutado
    K5 = round(len(proDataSet)/5)
    i=0

    PARTE = 1 #para saber en que subconjunto nos encontramos
    proDataSet["prueba "+str(PARTE)] = " "
    proDataSet["entreno "+str(PARTE)] = proDataSet["indice permutado"]
    while(i<len(proDataSet)):
        if(i==K5 and PARTE!=5):
            PARTE+=1
            proDataSet["prueba "+str(PARTE)] = " "
            proDataSet["entreno "+str(PARTE)] = proDataSet["indice permutado"]
            K5= round(len(proDataSet)/5)*PARTE
        proDataSet.at[i,"prueba "+str(PARTE)] = proDataSet.iloc[i]["indice permutado"]
        proDataSet.at[i,"entreno "+str(PARTE)] = None
        i+=1
    print(proDataSet)
    path = 'validacion_cruzada\\'
    proDataSet.to_csv(os.path.join(path,'Validacion.csv'))