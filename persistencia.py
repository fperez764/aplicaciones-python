# Persistencia de datos
# Entrada  lista de usuarios
# Salida Usuarios en formato JSON

import json

def guardar(datos, archivo="usuarios.json"):
 	with open(archivo, "w", encoding="utf-8") as f:
 		json.dump(datos, f, indent=4)

def cargar(archivo="usuarios.json"):
 	try:
 		with open(archivo, "r", encoding="utf-8") as f:
 			return json.load(f)
 	except FileNotFoundError:
 		return[]

# Pruebas
usuarios = [{"nombre":"Juan","email":"juan@mail.com","activo":True}]

guardar(usuarios)
print(cargar())