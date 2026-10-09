import json
mensaje = {
    "emisor": "Alejandro",
    "contenido": "Hola clase",
    "etiquetas": ("a", "b")
}

texto = json.dumps(mensaje, ensure_ascii=False)

print(texto)

copia = json.loads(texto)

print(f"Texto cargado: {copia}")

print("\n")

print(f"son iguales: {mensaje == copia}")
