from servicios.ServicioAbstracto import ServicioAbstracto
import os, logging

class ConsultaRegistros(ServicioAbstracto):
    def run():
        # ejecuta los comandos de la peticion
        os.system('python3 consultas.py --registros > ouputs.txt')
        logging.info('el output de peticion a sido escrito en el archivo outputs.tx')
        print('comando consultar registros ejecutado con exito')


        logging.info('todo correcto en el servidor')
        mensaje_servidor = ('comando consulta ejecutado con exito')
        
        return mensaje_servidor
