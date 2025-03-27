
# Función para modificar la ciudad dentro del diccionario
def modificar_datos(informacion_personal):
    modificar_ciudad = input("¿Desea modificar la ciudad? si/no: ")  # Pregunta al usuario si quiere cambiar la ciudad
    if modificar_ciudad == "si":  # Si el usuario responde que sí
        ciudad_actual_en_la_que_vive = input("Ingrese la ciudad actual en la que vive: ")  # Solicita la nueva ciudad
        informacion_personal["ciudad"] = ciudad_actual_en_la_que_vive  # Actualiza el valor de la clave "ciudad" en el diccionario
        print(informacion_personal)  # Muestra el diccionario modificado
    else:
        print("continuar")  # Muestra un mensaje para continuar sin modificaciones

# Función para añadir datos al diccionario
def añadir_datos(informacion_personal):
    añadir_datos = input("¿Desea añadir información adicional? si/no: ")  # Pregunta al usuario si quiere añadir información
    if añadir_datos == "si":  # Si el usuario responde que sí
        dato_agregado = input("Ingrese la categoría del dato que desea agregar: ")  # Solicita la nueva categoría
        informacion_personal[dato_agregado] = input("Ingrese el dato que desea agregar dentro de la categoría: ")  # Añade el nuevo dato al diccionario
        print(informacion_personal)  # Muestra el diccionario actualizado
    else:
        print("continuar")  # Muestra un mensaje para continuar sin añadir información

# Función para verificar si una categoría existe en el diccionario
def saber_si_esta_una_categoria(informacion_personal):
    saber_si_esta_una_categoria = input("¿Desea saber sobre alguna categoría en específico? si/no: ")  # Pregunta si quiere buscar una categoría
    if saber_si_esta_una_categoria == "si":  # Si el usuario responde que sí
        categoria_a_buscar = input("Ingrese la categoría a buscar: ")  # Solicita la categoría a buscar
        resultado_de_la_busqueda = categoria_a_buscar in informacion_personal  # Verifica si la categoría existe en el diccionario
        print(resultado_de_la_busqueda)  # Muestra True si la categoría existe, False si no
    else:
        print("continuar")  # Muestra un mensaje para continuar sin buscar categorías

# Función para eliminar datos del diccionario
def eliminar_un_dato(informacion_personal):
    dato_a_eliminar = input("¿Desea eliminar un dato? si/no: ")  # Pregunta si quiere eliminar algún dato
    if dato_a_eliminar == "si":  # Si el usuario responde que sí
        dato_eliminado = input("Ingrese la categoría a eliminar: ")  # Solicita la categoría a eliminar
        del informacion_personal[dato_eliminado]  # Elimina la categoría del diccionario
        print(informacion_personal)  # Muestra el diccionario actualizado
    else:
        print("salir")  # Muestra un mensaje de salida
    print("Culminación de ingreso de datos")  # Mensaje final tras completar las acciones

# Definición del diccionario con información inicial
informacion_personal = {"nombre": "Ana", "edad": 24, "ciudad": "Santa Cecilia", "profesion": "contadora"}  # Diccionario inicial
print(informacion_personal)  # Muestra el diccionario inicial
print("*"*50)  # Separador visual
modificar_datos(informacion_personal)  # Llama a la función para modificar datos
print("*"*50)  # Separador visual
añadir_datos(informacion_personal)  # Llama a la función para añadir datos
print("*"*50)  # Separador visual
saber_si_esta_una_categoria(informacion_personal)  # Llama a la función para verificar categorías
print("*"*50)  # Separador visual
añadir_datos(informacion_personal)  # Llama nuevamente a la función para añadir datos
print("*"*50)  # Separador visual
eliminar_un_dato(informacion_personal)  # Llama a la función para eliminar un dato