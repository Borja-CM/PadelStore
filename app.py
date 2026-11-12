
from fastapi import FastAPI
from productos import obtener_productos_bd, obtener_producto_por_id
from pydantic import BaseModel, Field
from productos import (
    obtener_productos_bd,
    obtener_producto_por_id,
    crear_producto_bd,
    eliminar_producto_bd,
    modificar_producto_bd
)



app = FastAPI(title="PadelStore")


# Define y valida los datos necesarios para crear o modificar un producto.
class ProductoNuevo(BaseModel):
    nombre: str = Field(min_length=2, max_length=150)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)




@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a PadelStore",
        "estado": "Tienda online en construccion"
    }


@app.get("/productos")
def listar_productos():
    return obtener_productos_bd()


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    producto = obtener_producto_por_id(producto_id)

    if producto is None:
        return {"error": "Producto no encontrado"}

    return producto


# Recibe los datos de un producto y lo guarda en MySQL.
@app.post("/productos")
def crear_producto(producto: ProductoNuevo):
    nuevo_producto = crear_producto_bd(
        producto.nombre,
        producto.precio,
        producto.stock
    )

    if nuevo_producto is None:
        return {"error": "No se pudo crear el producto"}

    return nuevo_producto


# Elimina un producto de la tienda utilizando su ID.
@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    resultado = eliminar_producto_bd(producto_id)

    if resultado is None:
        return {"error": "No se pudo eliminar el producto"}

    if not resultado:
        return {"error": "Producto no encontrado"}

    return {"mensaje": "Producto eliminado correctamente"}


# Recibe los nuevos datos y actualiza un producto existente.
@app.put("/productos/{producto_id}")
def modificar_producto(producto_id: int, producto: ProductoNuevo):
    resultado = modificar_producto_bd(
        producto_id,
        producto.nombre,
        producto.precio,
        producto.stock
    )

    if resultado is None:
        return {"error": "No se pudo modificar el producto"}

    if not resultado:
        return {"error": "Producto no encontrado"}

    return {"mensaje": "Producto modificado correctamente"}


