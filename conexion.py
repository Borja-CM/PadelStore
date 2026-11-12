import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():

    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if conexion.is_connected():
            print("Conexion con MySQL establecida correctamente.")
            return conexion

    except Error as error:
        print(f"Error al conectar con MySQL: {error}")
        return None

if __name__ == "__main__":
    conexion = obtener_conexion()

    if conexion:
        conexion.close()
        print("Conexion cerrada correctamente.")