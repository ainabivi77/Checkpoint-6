class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña


usuario1 = Usuario('Thomas', '98765')

print(usuario1.nombre_usuario)
print(usuario1.contraseña)