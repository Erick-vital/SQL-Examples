from abc import ABC, abstractclassmethod

class ServicioAbstracto(ABC):
    # todo metodo con el decorador abstraclassmethod
    #tiene que ser sobreescrito en la nueva clase
    
    @abstractclassmethod
    def run(self):
        pass