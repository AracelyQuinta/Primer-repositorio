# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento multiplicando el monto total por el porcentaje en formato decimal
    descuento = monto_total * (porcentaje_descuento / 100)
    # Retorna el monto del descuento
    return descuento


# Función para insertar datos de la factura
def insertar_datos_de_la_factura():
    # Inicializa una lista vacía para almacenar los productos de la factura
    factura = []
    # Variable para controlar si el usuario desea seguir ingresando más productos
    continuar = "si"
    # Bucle que permite ingresar múltiples productos mientras el usuario lo desee
    while continuar.lower() == "si":
        # Solicita al usuario ingresar la cantidad del producto
        cantidad = int(input("Ingrese la cantidad: "))
        # Solicita al usuario describir el producto
        descripcion = input("Ingrese qué ha comprado el cliente: ")
        # Solicita al usuario el precio unitario del producto
        precio_unitario = float(input("Ingrese el precio unitario: "))
        # Calcula el precio total multiplicando la cantidad por el precio unitario
        precio_total = cantidad * precio_unitario

        # Agrega los datos ingresados como un diccionario a la lista de factura
        factura.append({
            "cantidad": cantidad,
            "descripcion": descripcion,
            "precio_unitario": precio_unitario,
            "precio_total": precio_total
        })

        # Pregunta al usuario si desea continuar ingresando más productos
        continuar = input("¿Insertará más datos a la factura? si/no: ")

    # Devuelve la lista completa de productos ingresados
    return factura


# Programa principal
def main():
    # Mensaje inicial que indica el comienzo del ingreso de datos de la factura
    print("Ingreso de datos para la factura:")
    # Llama a la función para insertar datos de la factura y guarda la lista de productos ingresados
    factura = insertar_datos_de_la_factura()

    # Calcula el monto total sumando los precios totales de todos los productos de la factura
    monto_total = sum(item["precio_total"] for item in factura)
    # Imprime un encabezado para mostrar los detalles de la factura
    print("\nFactura Generada:")
    # Recorre cada producto en la factura para mostrar sus detalles
    for item in factura:
        print(
            f"{item['cantidad']} x {item['descripcion']} - ${item['precio_unitario']} c/u - Total: ${item['precio_total']}")
    # Muestra el monto total de la factura antes de aplicar descuentos
    print(f"Monto total sin descuento: ${monto_total}\n")

    # Primera llamada a la función calcular_descuento usando el porcentaje predeterminado (10%)
    descuento1 = calcular_descuento(monto_total)
    # Calcula el monto final restando el descuento al monto total
    monto_final1 = monto_total - descuento1
    # Muestra el monto del descuento aplicado y el monto final después del descuento
    print(f"Descuento aplicado (10% predeterminado): ${descuento1}")
    print(f"Monto final después del descuento: ${monto_final1}\n")

    # Solicita al usuario que ingrese un porcentaje de descuento personalizado
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento que desea aplicar: "))
    # Segunda llamada a la función calcular_descuento con el porcentaje ingresado por el usuario
    descuento2 = calcular_descuento(monto_total, porcentaje_descuento)
    # Calcula el monto final restando el nuevo descuento al monto total
    monto_final2 = monto_total - descuento2
    # Muestra el monto del descuento aplicado y el monto final después del descuento
    print(f"Descuento aplicado ({porcentaje_descuento}%): ${descuento2}")
    print(f"Monto final después del descuento: ${monto_final2}")


# Punto de entrada del programa: se asegura de que el programa principal se ejecute solo si se llama directamente
if __name__ == "__main__":
    # Llama al programa principal
    main()