# Definimos la función para calcular el promedio mensual.
def obtener_promedio_mensual(temperaturas, ciudad_nombre):
    """
    Calcula el promedio mensual de la ciudad ingresada utilizando los datos de temperaturas.

    Args:
        temperaturas (list): Lista 3D con las temperaturas por ciudad, semana y día.
        ciudad_nombre (str): Nombre de la ciudad para la cual se desea calcular el promedio mensual.

    Returns:
        dict o str: Diccionario con el promedio semanal y mensual si la ciudad existe,
        o un mensaje indicando que no se encuentra.
    """
    # Lista de ciudades por índice
    ciudades = ["GUAYAQUIL", "CUENCA", "LOJA"]

    # Validar si la ciudad ingresada está en la lista
    if ciudad_nombre.upper() not in ciudades:
        # Retorna un mensaje indicando que la ciudad no se encuentra en los datos.
        return f"La ciudad {ciudad_nombre} no se encuentra en los datos."

    # Obtener el índice de la ciudad
    ciudad_idx = ciudades.index(ciudad_nombre.upper())

    # Obtener las temperaturas de esa ciudad
    ciudad_temperaturas = temperaturas[ciudad_idx]

    # Inicializamos una lista para guardar los promedios semanales.
    promedios_semanales = []
    for semana in ciudad_temperaturas:  # Recorremos las temperaturas semana a semana.
        suma_temperaturas = sum([dia["temp"] for dia in semana])  # Sumamos las temperaturas de cada día en la semana.
        promedio = suma_temperaturas / len(semana)  # Calculamos el promedio semanal.
        promedios_semanales.append(promedio)  # Guardamos el promedio semanal en la lista.

    # Calculamos el promedio mensual como el promedio de los promedios semanales.
    promedio_mensual = sum(promedios_semanales) / len(promedios_semanales)

    # Retornamos un diccionario con los resultados.
    return {
        "Ciudad": ciudad_nombre.capitalize(),  # Nombre de la ciudad con la primera letra en mayúscula.
        "Promedios Semanales": promedios_semanales,  # Lista de promedios semanales.
        "Promedio Mensual": promedio_mensual  # Promedio mensual.
    }


# Función para mostrar los resultados de la ciudad seleccionada.
def mostrar_resultados(resultado):
    """
    Muestra los resultados de los promedios semanales y el promedio mensual para la ciudad dada.

    Args:
        resultado (dict): Diccionario con los datos de la ciudad, promedios semanales y mensual.
    """
    # Mostramos el nombre de la ciudad.
    print(f"Resultados para {resultado['Ciudad']}:")
    # Etiqueta indicando que mostramos los promedios semanales.
    print("Promedios Semanales:")
    # Iteramos sobre los promedios semanales para mostrarlos de manera formateada.
    for semana_idx, promedio_semanal in enumerate(resultado["Promedios Semanales"]):
        # Mostramos el promedio semanal indicando el número de la semana.
        print(
            f"Promedio de temperaturas en la Ciudad de {resultado['Ciudad']}, "
            f"Semana {semana_idx + 1}: {promedio_semanal:.2f} °C (grados celsius)"
        )
    # Mostramos el promedio mensual formateado con dos decimales.
    print(f"Promedio del mes de Enero: {resultado['Promedio Mensual']:.2f}°C")


# Función para realizar la interacción de búsqueda con el usuario.
def realizar_busqueda(temperaturas):
    """
    Realiza la búsqueda interactiva de los promedios semanales y mensuales para las ciudades disponibles.

    Args:
        temperaturas (list): Lista 3D con los datos de temperaturas por ciudad, semana y día.
    """
    while True:  # Permitimos al usuario realizar múltiples búsquedas.
        # Solicitamos al usuario que ingrese una ciudad.
        ciudad_consultada = input("Ingrese la ciudad: ").upper()
        # Llamamos a la función para obtener los resultados de la ciudad seleccionada.
        resultado = obtener_promedio_mensual(temperaturas, ciudad_consultada)
        if isinstance(resultado, dict):  # Verificamos si el resultado es válido (es un diccionario).
            mostrar_resultados(resultado)  # Mostramos los resultados llamando a la función correspondiente.
        else:
            # Si la ciudad no está en los datos, mostramos el mensaje de error devuelto por la función.
            print(resultado)

        # Preguntamos al usuario si desea realizar otra búsqueda.
        consultada1 = input("¿Quisiera seguir buscando? (si/no): ").lower()
        if consultada1 != "si":
            # Si el usuario no desea continuar, mostramos un mensaje de despedida y salimos del bucle.
            print("Fin de la búsqueda")
            break


# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [  # Ciudad : Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 35}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [  # Ciudad : cuenca
        [  # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [  # Ciudad : Loja
        [  # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 4
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

# Mensaje de bienvenida
print("Bienvenido al programa de búsqueda de promedios mensuales de temperaturas")
print("Puede ingresar el nombre de una ciudad (Guayaquil, Cuenca o Loja) para consultar los datos.")

# Llamamos a la función principal para iniciar las búsquedas.
realizar_busqueda(temperaturas)
