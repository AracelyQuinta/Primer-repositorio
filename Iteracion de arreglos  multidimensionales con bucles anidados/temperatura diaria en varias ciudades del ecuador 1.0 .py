# Definimos la función para calcular el promedio mensual.
def obtener_promedio_mensual(temperaturas, ciudad_nombre):
    """
    Calcula el promedio mensual de la ciudad ingresada utilizando los datos de temperaturas.

    Args:
        temperaturas (list): Lista 3D con las temperaturas por ciudad, semana y día.
        ciudad_nombre (str): Nombre de la ciudad para la cual se desea calcular el promedio mensual.

    Returns:
        dict o str: Promedio semanal y mensual de la ciudad si existe, caso contrario un mensaje.
    """
    # Lista de ciudades por índice
    ciudades = ["GUAYAQUIL", "CUENCA", "LOJA"]

    # Validar si la ciudad ingresada está en la lista
    if ciudad_nombre.upper() not in ciudades:
    #Se retorna el nombre de la ciudad de que no existe
        return f"La ciudad {ciudad_nombre} no se encuentra en los datos."

    # Obtener el índice de la ciudad
    ciudad_idx = ciudades.index(ciudad_nombre)

    # Obtener las temperaturas de esa ciudad
    ciudad_temperaturas = temperaturas[ciudad_idx]

    # Inicializamos una lista para guardar los promedios semanales.
    promedios_semanales = []
    for semana in ciudad_temperaturas:  # Recorremos las temperaturas semana a semana.
        suma_temperaturas = sum([dia["temp"] for dia in semana])  # Sumamos las temperaturas de cada día en la semana.
        promedio = suma_temperaturas / len(semana)  # Calculamos el promedio semanal.
        promedios_semanales.append(promedio)  # Guardamos el promedio semanal en la lista.

    # Calculamos el promedio mensual como el promedio de los promedios semanales.
    # Calcular el promedio mensual de la ciudad
    promedio_mensual = sum(promedios_semanales) / len(promedios_semanales)

    # Retornamos un diccionario con los resultados.
    return {
        "Ciudad": ciudad_nombre,  # Nombre de la ciudad.
        "Promedios Semanales": promedios_semanales,  # Lista de promedios semanales.
        "Promedio Mensual": promedio_mensual  # Promedio mensual.
    }
# Mensaje de bienvenida al usuario
print("Bienvenido al programa de busqueda de promedios mensuales de temperaturas")
print("Ingrese la ciudad para buscar los promedios mensuales:")
print("1. Guayaquil")
print("2. Cuenca")
print("3. Loja")
# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Ciudad : Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [   # Ciudad : cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [   # Ciudad : Loja
        [   # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 24}
        ]
    ]
]

# Llamada a la función para probar
ciudad_consultada = input("Ingrese la ciudad: ")  # 1.Solicitar ciudad al usuario.
# Llamamos a la función para calcular el promedio mensual
resultado = obtener_promedio_mensual(temperaturas, ciudad_consultada.upper())  # Obtener los datos de la ciudad seleccionada.

# Mostrar los resultados
if isinstance(resultado, dict):  # Verificar si el resultado es válido (es un diccionario).
            print(f"Resultados para {resultado['Ciudad']}:")  # Mostrar el nombre de la ciudad.
            print("Promedios Semanales:")  # Etiqueta para los promedios semanales.

            # Iterar sobre los promedios semanales y mostrar cada uno formateado.
            # Iteramos sobre los índices y los promedios semanales de la ciudad seleccionada.
            for semana_idx, promedio_semanal in enumerate(resultado["Promedios Semanales"]):
                # Imprimimos el promedio semanal con formato, indicando la semana correspondiente.
                    print( f"Promedio de temperaturas en la Ciudad de {resultado['Ciudad']}, "f"Semana {semana_idx + 1}: {promedio_semanal:.2f} °C (grados celsius)")
                    # Imprimimos el promedio mensual de la ciudad seleccionada con formato
                    # Mostrar el promedio mensual.
            print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")

            # Solicitamos al usuario que indique si desea realizar otra búsqueda.
            consultada1 = input("¿Quisiera seguir buscando? (si/no): ")

            # Iteramos sobre la respuesta ingresada por el usuario.
            for consulta in (consultada1):
                # Comprobamos si la respuesta del usuario es "si".
               if consultada1 == "si":
                 ciudad_consultada = input("Ingrese la ciudad: ")  # Solicitar ciudad al usuario.
                 resultado = obtener_promedio_mensual(temperaturas,ciudad_consultada.upper())  # Obtener los datos de la ciudad seleccionada.
                 # Mostrar los resultados
                 if isinstance(resultado, dict):  # Verificar si el resultado es válido (es un diccionario).
                        print(f"Resultados para {resultado['Ciudad']}:")  # Mostrar el nombre de la ciudad.
                        print("Promedios Semanales:")  # Etiqueta para los promedios semanales.
                        # Iterar sobre los promedios semanales y mostrar cada uno formateado.
                        for semana_idx, promedio_semanal in enumerate(resultado["Promedios Semanales"]):
                            print(f"Promedio de temperaturas en la Ciudad de {resultado['Ciudad']}, "f"Semana {semana_idx + 1}: {promedio_semanal:.2f} °C (grados celsius)")
                        # Mostrar el promedio mensual.
                        print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")
                        consultada1 = input("¿Quisiera seguir buscando? (si/no): ")
               else:
                # Si el usuario no desea seguir buscando o si no se cumple alguna otra condición,
                # se imprime un mensaje indicando que la búsqueda ha finalizado.
                 print("Fin de la busqueda")

else:
    # Si la ciudad no está en los datos, mostramos el mensaje de error devuelto por la función.
    print(resultado)
    # Solicitamos al usuario si desea buscar otra ciudad.
    consultada1 = input("¿Quisiera seguir buscando? (si/no): ")
     # Iteramos sobre los caracteres en la respuesta del usuario.
    for consulta in (consultada1):  # (Nota: este bucle procesa cada carácter de la respuesta, aunque no es necesario aquí).
        # Verificamos si la respuesta ingresada es "si".
        if consultada1 == "si":
            # Solicitamos al usuario que ingrese otra ciudad para buscar.
            ciudad_consultada = input("Ingrese la ciudad: ")
            # Llamamos nuevamente a la función para obtener los datos de la ciudad seleccionada.
            resultado = obtener_promedio_mensual(temperaturas, ciudad_consultada.upper())
            # Mostramos los resultados si la ciudad es válida.
            if isinstance(resultado, dict):  # Verificamos si el resultado es un diccionario (es decir, válido).
                # Mostramos el nombre de la ciudad.
                print(f"Resultados para {resultado['Ciudad']}:")
                # Etiqueta indicando que mostramos los promedios semanales.
                print("Promedios Semanales:")
                # Iteramos sobre los promedios semanales para mostrarlos de manera formateada.
                for semana_idx, promedio_semanal in enumerate(resultado["Promedios Semanales"]):
                    # Mostramos el promedio semanal indicando el número de la semana.
                    print(f"Promedio de temperaturas en la Ciudad de {resultado['Ciudad']}, "f"Semana {semana_idx + 1}: {promedio_semanal:.2f} °C (grados celsius)")
                # Mostramos el promedio mensual formateado con dos decimales.
                print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")
                # Preguntamos nuevamente si desea continuar buscando.
                consultada1 = input("¿Quisiera seguir buscando? (si/no): ")
        else:
           # Si la respuesta no es "si", finalizamos el programa con un mensaje de despedida.
           print("Fin de la busqueda")