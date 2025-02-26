# Crear una matriz bidimensional
matriz = [
    [5,6,10],
    [7,4,3],
    [4,9,2]
]
# Valor que estamos buscando

valor_a_buscar = 3

# Inicializar variables para rastrear la posición del valor
fila_en_la_que_se_encuentra = -1
columna_en_la_que_se_encuentra = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz [fila][columna] == valor_a_buscar:
            fila_en_la_que_se_encuentra = fila
            columna_en_la_que_se_encuentra = columna
            break # Detener la búsqueda una vez que se encuentra el valor
    if fila_en_la_que_se_encuentra != -1:
        break # Salir del bucle exterior si se encuentra el valor
# Verificar si se encontró el valor y mostrar la posición
if fila_en_la_que_se_encuentra != -1:
    print(f"Se encontró {valor_a_buscar} en la fila {fila_en_la_que_se_encuentra} y columna {columna_en_la_que_se_encuentra}.")
else:
    print(f"{valor_a_buscar} no se encontró en la matriz.")
