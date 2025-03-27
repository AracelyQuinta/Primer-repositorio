# Definición del diccionario con información inicial
diccionario= {"nombre":"Ana", "edad": 24, "ciudad": "Santa Cecilia", "profesion": "contadora"}
print(diccionario)

print("*"*20) # Separador visual

# Modificación de la clave "ciudad", actualizacion
diccionario["ciudad"]="Nueva Loja"
print(diccionario)
print("*"*20) # Separador visual

# Adición de una nueva clave "profesion2" con el valor "Enfermera"
diccionario["profesion2"]="Enfermera"
print(diccionario)
print("*"*20) # Separador visual

# Verificación de si la clave "telefono" existe en el diccionario
print("telefono" in diccionario)
print("*"*20) # Separador visual

# Adición de la clave "telefono" con el valor asignado
diccionario["telefono"]= "0991478591"
print(diccionario)
print("*"*20) # Separador visual

# Eliminación de la clave "edad" del diccionario
del diccionario["edad"]
print(diccionario)