""" Presenta falla abrutamente o se bloquea
Falta la proteccion en el if __name__ == "__main__"
Faltaria agregar el  if __name__ == "__main__" para proteger del codigo.
"""

from concurrent.futures import ProcessPoolExecutor


def cuadrado(n):
    return n * n


with ProcessPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(cuadrado, range(4))))