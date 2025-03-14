def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Nueva York": [22, 25, 26, 24, 23],
    "Los Ángeles": [28, 30, 29, 31, 27],
    "Chicago": [21, 20, 22, 18, 19],
    "Miami": [32, 33, 34, 30, 32],
    "Dallas": [26, 28, 27, 29, 25]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")


# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

##
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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = [" en la Ciudad de Guayaquil", " en la Ciudad de Cuenca ", " en la Ciudad de Loja"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} °C (grados celsius)")
