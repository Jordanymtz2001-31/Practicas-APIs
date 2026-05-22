from fastapi import APIRouter, HTTPException
from src.services.api_producto import get_productos

"""
Creamos una instancia de la clase APIRouter
Estamos creando un contenedor de endpoints o rutas
Luego en el main podermos importarlos con routers
"""
router = APIRouter() 


# Definimos el endpoint con un decorador router de tipo GET para despues llamarlo en el main
@router.get("/", response_model=list[dict]) # El response_model indica que el endpoint devuelve una lista de diccionarios
async def list_products():    
    try:
        return await get_productos() # Llamamos a la funcion get_productos para obtener los productos de la API y los devolvemos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) # Si la peticion falla lanza un error