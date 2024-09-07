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

#Datos de usuarios
usuarios={
    "admin":"clave1234",
    "Joel":"clave5678",
    "Diego":"clave9876"
}



#Definir funcion de inicio de sesion
@app.post("/login/")
def login(usuario, clave):
  #mensaje="Bienvenido"
  if usuario in usuarios:
    mensaje="usuario correcto"
    if len(clave)>=8:
      mensaje="clave correcta"
      if clave==usuarios[usuario]:
        mensaje=f"Inicio de sesion exitoso. Bienvenido {usuario}"
      else:
        mensaje="clave incorrecta"
    else:
      mensaje="clave incorrecta, debe tener al menos 8 caracteres"
  else:
    mensaje="usuario no encontrado"
  return mensaje
#Programa principal
print(login("admin","clave1234"))
print(login("Diego","clave9876"))


