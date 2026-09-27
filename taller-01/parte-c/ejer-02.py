"""Trabajo secuencial tarda cerca de 3.2 segundos
Se debe cambiar el metodo start por run y agregar el constructor super
"""

import threading
import time


class Tarea(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        time.sleep(1)
        print(self.name, "lista")


inicio = time.perf_counter()
tareas = [Tarea(name=f"t{i}") for i in range(3)]
for t in tareas:
    t.start()
print(f"{time.perf_counter() - inicio:.1f} s")
for t in tareas:
    t.join()