from abc import ABC, abstractclassmethod
import logging
import os
from dotenv import load_dotenv
import hmac
import hashlib
import json
import pickle


load_dotenv()
private_key = os.getenv('p_k').encode()

class AbstractaSertvidor(ABC):
    # todo metodo con el decorador abstraclassmethod
    #tiene que ser sobreescrito en la nueva clase
    def __init__(self, parameters):
        self.parameters = parameters
        self.msg_json = json.loads(pickle.loads(self.parameters))
        self.sign = self.msg_json.pop("sign")
        self.actual_digest = hmac.new(private_key, str(self.msg_json).encode(), hashlib.sha256).hexdigest()
    
    @abstractclassmethod
    def run(self):
        pass

class Consultas(AbstractaSertvidor):
    def run(self):
        # compara que las llaves sean correctas
        if hmac.compare_digest(self.actual_digest, self.sign):
            # ejecuta los comandos de la peticion
            if self.msg_json["peticion"] == 'consulta':
                os.system('python3 consultas.py --order > ouputs.txt')
                os.system('python3 consultas.py --registros >> ouputs.txt')
                logging.info('el output de peticion a sido escrito en el archivo outputs.tx')
                print('comandos ejecutados con exito')
            elif self.msg_json["peticion"] == 'crear':
                os.system('python3 consultas.py --tabla')
                os.system('python3 consultas.py --procedimiento')
                logging.info('comandos ejecutados con exito')
                print('comandos ejecutados con exito')

            logging.info('todo correcto en el servidor')
            mensaje_servidor = ('todo correcto en el servidor')
        else:
            print('peligro posible corrupcion de datos')
            logging.info('peligro posible corrupcion de datos')
            mensaje_servidor = ('peligro posible corrupcion de datos')
        
        return mensaje_servidor
