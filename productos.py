from mysql.connector import Error


# Funcion para mostrar los productos de la BBDD
def mostrar_productos():

    print("\n--- CATALOGO DE PADELSTORE ---")

    productos_bd = obtener_productos_bd()

    if not productos_bd:
        print("No hay productos disponibles.")
        return

    for producto in productos_bd:
        print("-----------------------------")
        print(f"ID: {producto['id']}")
        print(f"Producto: {producto['nombre']}")
        print(f"Precio: {producto['precio']:.2f} euros")
        print(f"Stock disponible: {producto['stock']} unidades")


# Funcion para agregar los productos

def agregar_producto():

    print("\n--- AÑADIR NUEVO PRODUCTO ---")

    nombre = input("Nombre del producto: ")

    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Precio del producto: "))
        stock = int(input("Unidades disponibles: "))

        if precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
            return

        if stock < 0:
            print("Error: el stock no puede ser negativo.")
            return

    except ValueError:
        print("Error: introduce un precio y un stock válidos.")
        return

    conexion = obtener_conexion()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:
        consulta = """
            INSERT INTO productos (nombre, precio, stock)
            VALUES (%s, %s, %s)
        """

        valores = (nombre, precio, stock)

        cursor.execute(consulta, valores)
        conexion.commit()

        print("\nProducto añadido correctamente.")
        print(f"ID asignado: {cursor.lastrowid}")

    except Error as error:
        print(f"Error al añadir el producto: {error}")

    finally:
        cursor.close()
        conexion.close()

# Creamos la funcion para eliminar productos

# Funcion para eliminar productos
def eliminar_producto():

    print("\n--- ELIMINAR PRODUCTO ---")

    try:
        id_buscar = int(input("ID del producto que quieres eliminar: "))
    except ValueError:
        print("Debes introducir un ID numérico.")
        return

    conexion = obtener_conexion()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:
        consulta = "DELETE FROM productos WHERE id = %s"
        cursor.execute(consulta, (id_buscar,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("Producto eliminado correctamente.")
        else:
            print("No existe ningún producto con ese ID.")

    except Error as error:
        print(f"Error al eliminar: {error}")

    finally:
        cursor.close()
        conexion.close()

# Funcion para modificar productos
def modificar_producto():

    print("\n--- MODIFICAR PRODUCTO ---")

    try:
        id_buscar = int(input("ID del producto que quieres modificar: "))
    except ValueError:
        print("Debes introducir un ID numérico.")
        return

    nombre = input("Nuevo nombre: ")

    if nombre.strip() == "":
        print("El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Nuevo precio: "))
        stock = int(input("Nuevo stock: "))

        if precio <= 0 or stock < 0:
            print("El precio debe ser positivo y el stock no puede ser negativo.")
            return

    except ValueError:
        print("Introduce valores numéricos válidos.")
        return

    conexion = obtener_conexion()

    if conexion is None:
        return

    cursor = conexion.cursor()

    try:
        consulta = """
            UPDATE productos
            SET nombre = %s, precio = %s, stock = %s
            WHERE id = %s
        """

        valores = (nombre, precio, stock, id_buscar)

        cursor.execute(consulta, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            print("Producto modificado correctamente.")
        else:
            print("No existe ningún producto con ese ID.")

    except Error as error:
        print(f"Error al modificar: {error}")

    finally:
        cursor.close()
        conexion.close()
    

# Establecer conexión con la BBDD directamente:
#  Se conecta a MYSQL
#  Ejecuta SELECT para obetener productos
#  Recupera resultados
#  Cierra conexion y los devuelve
from conexion import obtener_conexion

def obtener_productos_bd():
    conexion = obtener_conexion()

    if conexion is None:
        return []

    cursor = conexion.cursor(dictionary=True) #cursor: objeto para enviar instrucciones MySQL y recibirlos los datos.

    cursor.execute(
        "SELECT id, nombre, precio, stock FROM productos ORDER BY id"
    )

    productos_bd = cursor.fetchall() #fetchall, obetemer los resultados de la consulta

    cursor.close()
    conexion.close()

    return productos_bd