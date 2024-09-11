from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from database import alumnos


app = FastAPI()

# Habilitar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen, cámbialo a una lista específica en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Definir función de inicio de sesión
@app.post("/login/")
def iniciarSesion(usuario: str, clave: str):
   return "Iniciar sesión"