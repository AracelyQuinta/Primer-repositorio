# Crear una matriz bidimensional (3x3)
matriz =[
    [20,102,10],
    [7,5,15],
    [18,32,38]
]
# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    n =len(fila)
    for i in range (n-1):
        for j in range(n-1-i):
            if fila[j]>fila[j+1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elemento

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)
            