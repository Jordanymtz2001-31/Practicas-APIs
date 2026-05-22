import httpx

FAKESTORE_URL = "https://fakestoreapi.com/products"

async def get_productos():
    async with httpx.AsyncClient() as client: #Para hacer peticiones asincronas usamos httpx
        response = await client.get(FAKESTORE_URL) # El await indica que la peticion es asincrona
        response.raise_for_status() #Si la peticion falla lanza un error
        return response.json()