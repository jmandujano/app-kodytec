from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Habilitar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen, cámbialo a una lista específica en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Modelo para la solicitud de login
class LoginRequest(BaseModel):
    username: str
    password: str

# Función para validar usuario y contraseña
@app.post("/login/")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "1234":
        return {"message": "Login successful", "user": request.username}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )
