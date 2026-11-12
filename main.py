
# Importamos las funciones del archivo productos.py
from productos import mostrar_productos, agregar_producto, eliminar_producto, modificar_producto, obtener_productos_bd


# ==================================
# PadelStore - Nuestra tienda online
# ==================================

def menu_administracion():

    print("================================")
    print("       BIENVENIDO A PADELSTORE")
    print("================================")

    print("Panel de administracion")

    while True:

        print("\n========== MENU ADMIN ==========")
        print("1. Ver productos")
        print("2. Añadir producto")
        print("3. Eliminar producto")
        print("4. Modificar producto")
        print("5. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            agregar_producto()

        elif opcion == "3":
            eliminar_producto()

        elif opcion == "4":
            modificar_producto()
        
        elif opcion == "5":
            print("Hasta pronto.")
            break

        else:
            print("Opcion no valida. Intentalo de nuevo.")


print("\n--- PRODUCTOS GUARDADOS EN MYSQL ---")

productos_mysql = obtener_productos_bd()

for producto in productos_mysql:
    print(producto)

# Iniciamos el programa
menu_administracion()


