"""Como no se llama al constructor super de la clase padre y no se inicializa el hilo
Se debe agregar el constructor super, por eso no se ejecuta el hilo 
y no se imprime el mensaje de descarga.
"""

import threading


class Descarga(threading.Thread):
    def __init__(self, archivo):
        super().__init__()
        self.archivo = archivo

    def run(self):
        print("descargando", self.archivo)


Descarga("a.zip").start()