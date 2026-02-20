# Validacion de campos 
# Si Nombre es vacio , correo es invalido ERROR

def validar_usuario(data):
 	error = []

 	if not data.get("nombre"):
 		error.append("Nombre es Requerido")

 	correo = data.get("correo")
 	if not correo or "@" not in correo:
 		error.append("Correo es Requerido o no cumple con formato")
 	return error

usuario = {
 	"nombre": "Amy Ariana",
 	"correo": "gabop764#gmail.com"
}

error = validar_usuario(usuario)

if error:
 	print("ERROR:",error)
else:
 	print("VALIDO")

