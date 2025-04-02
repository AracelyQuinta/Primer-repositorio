def insertar_informacion():
    # Solicita al usuario si desea insertar información adicional
    verificacion = input("¿Insertar información adicional? (si/no): ").strip().lower()

    if verificacion == "si":  # Si el usuario responde "si"
        contenido = input("Ingrese información: ")  # Solicita el contenido a agregar
        # Ruta del archivo al que se desea escribir y leer
        ruta = "C:/Users/HP - i5/Downloads/2425---FUNDAMENTOS-DE-PROGRAMACION----UEA-L-UFB-026/Primer-repositorio/ operaciones de lectura y escritura en archivos de texto/my_notes1.txt"

        # Abre el archivo en modo "w" (escritura) para reemplazar el contenido existente
        archivo = open(ruta, "w")  # Modo "w" elimina el texto anterior y escribe desde cero
        archivo.write(contenido + "\n")  # Escribe el nuevo contenido
        archivo.close()  # Cierra el archivo después de escribir
        print("----Texto actualizado en archivo----")  # Informa que el texto fue reemplazado

        # Abre nuevamente el archivo en modo lectura para mostrar contenido actualizado
        archivo = open(ruta, "r")
        print("----Contenido actualizado del archivo----")
        print(archivo.read())  # Imprime el contenido actualizado del archivo
        archivo.close()
    else:
        print("No se insertó información adicional.")

def establecer_archivo(ruta, permiso):
    # Abre un archivo con la ruta y el permiso especificados y lo retorna
    archivo = open(ruta, permiso)
    return archivo

def leer_archivo(archivo):
    # Lee  el contenido del archivo
    contenido = archivo.read()
    return contenido

def escribir_archivo(archivo, texto):
    # Escribe texto en el archivo
    archivo.write(texto)


# Abre el archivo utilizando la función establecer_archivo
arch = establecer_archivo("C:/Users/HP - i5/Downloads/2425---FUNDAMENTOS-DE-PROGRAMACION----UEA-L-UFB-026/Primer-repositorio/ operaciones de lectura y escritura en archivos de texto/my_notes1.txt","r+")
print("-----lectura del archivo-----")
print(leer_archivo(arch))  # Lee y muestra el contenido inicial del archivo
print("*" * 20)
insertar_informacion()  # Llama a la función para insertar información adicional
print("*" * 20)  # Otra línea de asteriscos
arch.close()  # Cierra el archivo después de terminar las operaciones