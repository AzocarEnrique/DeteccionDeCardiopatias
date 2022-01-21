import random
def balance(proDataSet):
    balanceDataSet = proDataSet
    balanceDataSet = balanceDataSet.groupby(['HeartDisease']).size().reset_index(name='count')## agrupa las filas por valores repetidos en "HeartDisease" y agrega una columna "count" para llevar la cuenta
    #######Ver cual dato de la clase es mayor
    if(balanceDataSet.iloc[0]['count']-balanceDataSet.iloc[1]['count']<0):
        x = 1
    elif(balanceDataSet.iloc[0]['count']-balanceDataSet.iloc[1]['count']>0):
        x = 0
    ####### iloc para ver el valor de la celda en especifico
    while(balanceDataSet.iloc[0]['count']!=balanceDataSet.iloc[1]['count']):
        randomNum = random.randrange(balanceDataSet.iloc[0]['count']+balanceDataSet.iloc[1]['count'])
        if(randomNum in proDataSet.index): ##comprobar si el numero random existe en el index
            if(proDataSet.iloc[randomNum]['HeartDisease']==x):
                proDataSet = proDataSet.drop([randomNum])##elimina una fila aleatoria que tenga HeartDisease con los datos más altos
                balanceDataSet.at[x,'count']=balanceDataSet.iloc[x]['count']-1
    proDataSet = proDataSet.reset_index(drop=True)
    return proDataSet