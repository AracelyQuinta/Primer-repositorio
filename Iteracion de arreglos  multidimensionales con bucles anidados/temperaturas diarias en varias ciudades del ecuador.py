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
