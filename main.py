from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen, cámbialo a una lista específica en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Datos de alumnos
alumnos = {
    'C1': {'clave': 'password123', 'nombre': 'Renzo', 'apellido': 'Santillán'},
    'C2': {'clave': 'securePass456', 'nombre': 'Julio', 'apellido': 'Mandujano'},
    'C3': {'clave': 'password789', 'nombre': 'Joel', 'apellido': 'Campos'}
}

# Definir función de inicio de sesión
@app.post("/login/")
def login(usuario: str, clave: str):
    if usuario in alumnos:        
        if clave == alumnos[usuario]['clave']:
            return {
                "is_success": True,
                "message": f"Bienvenido {alumnos[usuario]['nombre']}",
                "data": [
                    {
                        "nombre": alumnos[usuario]['nombre'],
                        "apellido": alumnos[usuario]['apellido']
                    }
                ]
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Clave incorrecta"
            )        
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

# Programa principal para pruebas
print(login(usuario="C1", clave="password123"))
print(login(usuario="C3", clave="password789"))
