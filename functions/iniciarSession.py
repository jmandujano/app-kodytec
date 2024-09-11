def iniciarSesion(usuario: str, clave: str):
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