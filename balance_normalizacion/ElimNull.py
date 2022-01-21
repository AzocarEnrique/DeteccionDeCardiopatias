def ElimNull(proDataSet):
    num=0
    x=0
    nombres= proDataSet.columns.tolist()##lista de nombres de las variables y clase
    while(x<len(proDataSet.columns)):##crear una lista con el nombre de la variable y su numero para mostrarlo en pantalla
        nombres[x]=str(x+1)+" "+nombres[x]##agregar su numero correspondiente
        x+=1
    while True: 
        try:
            print(nombres)
            num = int(input("Lista de variables\n¿Que variables no pueden contener 0 en sus celdas, escoja un numero correspondiente a la variable para limpiarla\nescoja cualquier otro para salir:"))
            if(0<num<13):
                proDataSet = proDataSet[proDataSet[proDataSet.dtypes.index[num-1]] != 0]
            else:
                break
        except ValueError:
            print("No es válido")
    proDataSet = proDataSet.reset_index(drop=True)
    return proDataSet