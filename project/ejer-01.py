import pickle
mensaje = {
    "emisor": "Alejandro",
    "contenido": "Hola clase",
    "etiquetas": ("a", "b")
}

datos = pickle.dumps(mensaje)
print(datos)

print("\n")

copia = pickle.loads(datos)
print(copia)