# Aqui creamos nuestros esquemas, es decir para mappear los datos que recibimos de la API
# Sirve para validar de que tipo de dato recibimos y para porteriormente los enviamos

# Importamos la libreria de pydantic para crear los esquemas
from pydantic import BaseModel

class Usuario(BaseModel):
    name: str
    edad: int