
from servicios.ServicioAbstracto import ServicioAbstracto
import os, logging

class CrearEntidad(ServicioAbstracto):
    def run():
        # ejecuta los comandos de la peticion
        os.system('python3 consultas.py --tabla')
        os.system('python3 consultas.py --procedimiento')
        logging.info('el output de peticion a sido escrito en el archivo outputs.tx')
        print('comando consultar registros ejecutado con exito')


        logging.info('todo correcto en el servidor')
        mensaje_servidor = ('comando Crear Entidad ejecutado con exito')
        
        return mensaje_servidor
