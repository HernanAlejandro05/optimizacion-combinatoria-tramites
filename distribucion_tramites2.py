import pandas as pd
tiempos = {
    16: 'T1',
    8: 'T2',
    4: 'T3',
    1: 'T4',
    0.5: 'T5'
}




def calcular_combinacion(duracion_pasantia, duracion_tramites, index=0):
    # Condicon de salida si duracion_pasantia es un valor negativo.
    if duracion_pasantia < 0:
        return []

    # Condicon de salida si duracion_pasantia es igual a cero.
    if duracion_pasantia == 0:
        return [{}]

    # Condicon de salida cuando no se envia la lista con la duracion de los tramites.
    if index == len(duracion_tramites):
        return []

    lista_soluciones = []
    duracion = duracion_tramites[index]
    tramites_por_pasantia = int(duracion_pasantia//duracion)

    # Busca las posibles soluciones para alcanzar la duracion de la pasantia.
    for tramites in range(tramites_por_pasantia + 1):

        soluciones = calcular_combinacion(  # Ejecuta la llamada recursiva.
            duracion_pasantia - tramites * duracion,
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
soluciones_96 = calcular_combinacion(96, [16, 8, 4, 1, 0.5])
#soluciones_160 = calcular_combinacion(160, [16, 8, 4, 1, 0.5])
#print(len(soluciones_96))
#print(soluciones_96)
print(len(soluciones_96))
print(soluciones_96)

df = pd.DataFrame.from_dict(soluciones_96).fillna(0)
print(df)
df.to_excel('combinaciones_96_fijas.xlsx')