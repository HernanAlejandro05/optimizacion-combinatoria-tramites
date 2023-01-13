import pandas as pd
tiempos = {
    16: 'T1', #---------> 16 h
    8: 'T2',  #--------->  8h
    4: 'T3',  #--------->  4h
    1: 'T4',  #--------->  1h
    0.5: 'T5' #--------->  0.5h
}


#la funcion  

def calcular_combinacion(duracion_pasantia, duracion_tramites, index=0):
    # Condicon de salida si duracion_pasantia es un valor negativo.
    if duracion_pasantia < 0:
        return []   #retorna lista vacia

    # Condicon de salida si duracion_pasantia es igual a cero.
    if duracion_pasantia == 0:
        return [{}] #devuelve un la lsita con diccionario

    # Condicon de salida cuando no se envia la lista con la duracion de los tramites.
    if index == len(duracion_tramites):
        return []  #devuelve lista vacia

    lista_soluciones = []   #  almacena todas lasposibles combianciones que van encontrando
    duracion = duracion_tramites[index] # va tomando cada duracion y realizando operaciones recursivas para verificar la suma total (160 o 96)
    tramites_por_pasantia = int(duracion_pasantia//duracion)  #Division que devuelve la parte entera y hace caso omiso a la parte decimal

    # Busca las posibles soluciones para alcanzar la duracion de la pasantia.
    for tramites in range(tramites_por_pasantia + 1):

        soluciones = calcular_combinacion(  # Ejecuta la llamada recursiva.
            duracion_pasantia - tramites * duracion,   #Termina cuando termina de encontrar todas las combinaciones
            duracion_tramites,
            index + 1
        )

        # Agrega las soluciones encontradas a la lista.
        for solucion in soluciones:
            if tramites > 0:
                sol2 = solucion.copy()   
                sol2[tiempos[duracion]] = tramites
            else:
                sol2 = solucion

            lista_soluciones.append(sol2)

    return lista_soluciones


# soluciones_96 = calcular_combinacion(8, [4, 1])
#soluciones_96 = calcular_combinacion(96, [16, 8, 4, 1, 0.5])
soluciones_160 = calcular_combinacion(160, [16, 8, 4, 1, 0.5])
#print(len(soluciones_96))
#print(soluciones_96)
print(len(soluciones_160))
print(soluciones_160)

df = pd.DataFrame.from_dict(soluciones_160).fillna(0) #de la libreria pandas, llamo a un dataframe para almacenar el diccionario 
df == 0  #Creo un dataframe booleano
df = df[~(df == 0).any(axis=1)]
print (df)
df.to_excel('combinaciones_160_fijas.xlsx')   #El diccionario  resultante se guarda en un archivo excel