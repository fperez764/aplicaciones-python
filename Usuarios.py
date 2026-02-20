# Gestion de Ususarios
# entrada nombre, email, activo.
# salida lista filtrada
# estructura principal 
usuarios = []
def validar_correo(correo):
	return "@" in correo and "." in correo

def add_usuario(nombre, correo, activo=True):
	if not validar_correo(correo):
		return "Correo INVALIDO"

	usuario = {
		"nombre": nombre,
		"correo": correo,
		"activo": activo
	}

	usuarios.append(usuario)
	return "USUARIO REGISTRADO CON EXITO"

def obtener_activos():
	return[u for u in usuarios if u["activo"]]	

# pruebas
print(add_usuario("Amy","amiariana@gmail.com"))
print(add_usuario("Rafael","rafa@aetn.gob.bo"))
print(add_usuario("nose que hace","nose@gmail.com",False))
print(obtener_activos())