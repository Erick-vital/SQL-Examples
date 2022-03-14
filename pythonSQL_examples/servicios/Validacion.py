import importlib
import json
from servicios.ServicioAbstracto import ServicioAbstracto
import hmac, logging, json, pickle, hashlib
import os
from dotenv import load_dotenv
from jsonrpcserver import Error

load_dotenv()
private_key = os.getenv('p_k').encode()


class Validacion(ServicioAbstracto):
    def __init__(self, parameters):
        self.parameters = parameters
        self.msg_json = json.loads(pickle.loads(self.parameters))
        self.sign = self.msg_json.pop("sign")
        self.actual_digest = hmac.new(private_key, str(self.msg_json).encode(), hashlib.sha256).hexdigest()

    # valida Firma
    def run(self):
        try:
            if hmac.compare_digest(self.actual_digest, self.sign):
                logging.info('todo correcto en el servidor')
                return True
        except Error as e:
            print('peligro posible corrupcion de datos {e}')
            logging.info('peligro posible corrupcion de datos {e}')
            return False
    
    def validar_comando(self):
        comandos = {
            'consulta': 'ConsultaRegistros',
            'crear': 'CrearEntidad',
        }

        comando = self.msg_json["peticion"]
        if comando in comandos:
            current_lib = importlib.import_module('servicios.' + comandos[comando])
            clase = getattr(current_lib, comandos[comando])
            return clase.run()
        else:
            return 'comando no encontrado'
