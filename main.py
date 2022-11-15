# Librerias


#python

#Pydantic 
from pydantic import BaseModel

#Fastapi
from fastapi import FastAPI


#Modelo
class Item(BaseModel): #Item Extiende de Base Model 
    name: str
    description: str | None = None #Atributos ops
    price: float
    tax: float | None = None


#Instancia
app = FastAPI()

#Methodos get

#Ruta Root
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Path Parametros ---> Obligatorios
@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id}

#Base de Datos Simulado
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#Query Parametros ---> ops 
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):

    #Traer Informacion de la base de datos
    return fake_items_db[skip : skip + limit]


# Methodo Post
@app.post("/items/")
async def create_item(item: Item):
#Logica de agregar item a la base de datos 
#con el modelo de item

    return item

