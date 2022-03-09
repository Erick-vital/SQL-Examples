import logging
import os
from dotenv import load_dotenv
import hmac
import hashlib
import asyncio
from cProfile import run
import websockets
import json
import pickle

load_dotenv()
private_key = os.getenv('p_k').encode()
host = os.getenv('host')
port = os.getenv('port')

async def main(websocket, path):
    mensaje = await websocket.recv()
    msg_json = json.loads(pickle.loads(mensaje))
    sign = msg_json.pop("sign")
    actual_digest = hmac.new(private_key, str(msg_json).encode(), hashlib.sha256).hexdigest()


    # compara que las llaves sean correctas
    if hmac.compare_digest(actual_digest, sign):
        # ejecuta los comandos de la peticion
        if msg_json["peticion"] == 'consulta':
            os.system('python3 consultas.py --order > ouputs.txt')
            os.system('python3 consultas.py --registros >> ouputs.txt')
            logging.info('el output de peticion a sido escrito en el archivo outputs.tx')
            print('comandos ejecutados con exito')
        elif msg_json["peticion"] == 'crear':
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

    await websocket.send(mensaje_servidor)

start_server = websockets.serve(main, host, port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
    
