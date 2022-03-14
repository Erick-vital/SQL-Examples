
import os, sys
from dotenv import load_dotenv
import asyncio
from cProfile import run
import websockets
sys.path.append('/home/tao/python/pythonSQL_ejemplos')
from servicios.Validacion import Validacion

load_dotenv()

private_key = os.getenv('p_k').encode()
host = os.getenv('host')
port = os.getenv('port')

async def main(websocket, path):
    mensaje = await websocket.recv()
    print(mensaje)
    # v = Validacion(mensaje)

    # if v.run():
    #     mensaje_servidor = v.validar_comando()
    # else:
    #     mensaje_servidor = 'error posible corrupcion de datos'

    await websocket.send(' que tal ')

start_server = websockets.serve(main, host, 5060)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
