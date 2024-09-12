from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse  # Importar JSONResponse
from database import alumnos  # Importar el diccionario alumnos
from functions.iniciarSesion import iniciarSesion  # Asegúrate de que el nombre del archivo y la importación sean correctos

app = FastAPI()

# Habilitar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen, cámbialo a una lista específica en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Ruta de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}

# Función de inicio de sesión
@app.post("/login/")
def login(codigo: str, clave: str):
    resultado = iniciarSesion(codigo, clave)
    if "Inicio de sesión exitoso" in resultado:
        return {
            "is_success": True,
            "message": resultado,
            "data": {
                "codigo": codigo,
                "nombre": alumnos[codigo]['nombre'],
                "apellido": alumnos[codigo]['apellido']
            }
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario no encontrado"
        )

# Manejo de excepciones personalizadas
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "is_success": False,
            "message": exc.detail,
            "data": None
        }
    )
