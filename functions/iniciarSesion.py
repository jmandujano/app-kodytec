from database import alumnos

def iniciarSesion(codigo: str, clave: str) -> str:
    if codigo in alumnos:
        if len(clave) >= 8:
            if clave == alumnos[codigo]['clave']:
                return f"Inicio de sesión exitoso. Bienvenido {alumnos[codigo]['nombre']} {alumnos[codigo]['apellido']}"
            else:
                return "Clave incorrecta"
        else:
            return "Clave incorrecta"
    else:
        return "Usuario no encontrado"

# Casos de prueba
print(iniciarSesion('C1', 'password123'))  # "Inicio de sesión exitoso. Bienvenido Renzo Santillán"
print(iniciarSesion('C2', 'wrongPass'))    # "Clave incorrecta"
print(iniciarSesion('C3', 'pass'))         # "Clave incorrecta"
print(iniciarSesion('C4', 'anyPassword'))  # "Usuario no encontrado"
print(iniciarSesion('C1', 'password'))     # "Clave incorrecta"
