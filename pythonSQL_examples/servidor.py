import os, sys
from dotenv import load_dotenv
import asyncio
from cProfile import run
import websockets
sys.path.append('/home/tao/python/pythonSQL_ejemplos/servicios')
from servicios.Validacion import Validacion

load_dotenv()

private_key = os.getenv('p_k').encode()
host = os.getenv('host')
port = os.getenv('port')

async def main(websocket, path):
    mensaje = await websocket.recv()
    v = Validacion(mensaje)

    if v.run():
        mensaje_servidor = v.validar_comando()
    else:
        mensaje_servidor = 'error posible corrupcion de datos'

    await websocket.send(mensaje_servidor)

start_server = websockets.serve(main, host, port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
