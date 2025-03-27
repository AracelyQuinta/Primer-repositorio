# Definición del diccionario con información inicial
informacion_personal= {"nombre":"Ana", "edad": 24, "ciudad": "Santa Cecilia", "profesion": "contadora"}
print(informacion_personal)

print("*"*20) # Separador visual

# Modificación de la clave "ciudad", actualizacion
informacion_personal["ciudad"]="Nueva Loja"
print(informacion_personal)
print("*"*20) # Separador visual

# Adición de una nueva clave "profesion2" con el valor "Enfermera"
informacion_personal["profesion2"]="Enfermera"
print(informacion_personal)
print("*"*20) # Separador visual

# Verificación de si la clave "telefono" existe en el diccionario
print("telefono" in informacion_personal)
print("*"*20) # Separador visual

# Adición de la clave "telefono" con el valor asignado
informacion_personal["telefono"]= "0991478591"
print(informacion_personal)
print("*"*20) # Separador visual

# Eliminación de la clave "edad" del diccionario
del informacion_personal["edad"]
print(informacion_personal)