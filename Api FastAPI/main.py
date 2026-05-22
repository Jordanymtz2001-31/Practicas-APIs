from fastapi import FastAPI
from src.schemas.usuario import Usuario
from fastapi.middleware.cors import CORSMiddleware #Para permitir peticiones de otros dominios
from src.routers.productos import router as router #Importamos el router y lo renombramos router


#CREACION DE NUESTRO PRIMER ENDPOINT

#Creamos una instancia de FastAPI
app = FastAPI()

# Ejemplo de configuracion para permitir peticiones de otros dominios

origin = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin, #Que origenes permitimos
    allow_credentials=True, #Que credenciales permitimos
    allow_methods=["*"], #Que metodos permitimos
    allow_headers=["*"], #Que headers permitimos
)

API_UR = "https://fakestoreapi.com/products"


#Definimos el endpoint
@app.get("/api/") # Con el decorador le indicamos que es un endpoint de tipo GET
async def read_root(): # async indica que el endpoint es asincrono
    return {"message": "Hello World"}


#Creamos un segundo endpoint
@app.post("/guardar/usuarios/")
async def guardar(objeto: Usuario): #Como parametro esperamos un objeto de tipo Usruario
    return {'name': objeto.name, 'edad': objeto.edad} 

"""
Definimos un tercer endpoint llamado al endpoint de productos que esta en routers
Con prefix le indicamos que el endpoint se va a llamar /products
Con el tags le indicamos que el endpoint pertenece a la categoria de productos
"""
app.include_router(router, prefix="/products", tags=["products"])