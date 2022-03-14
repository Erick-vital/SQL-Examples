import os, sys, asyncio, websockets
from dotenv import load_dotenv
from cProfile import run
sys.path.append('/home/tao/python/pythonSQL_ejemplos')
from servicios.Validacion import Validacion

load_dotenv()

private_key = os.getenv('p_k').encode()
host = os.getenv('host')
port = os.getenv('port')

async def main(websocket, path):
    mensaje = await websocket.recv()
    v = Validacion(mensaje)

    if v.run():
        mensaje_servidor = 'servidor1' + v.validar_comando()
    else:
        mensaje_servidor = ' servidor1 error posible corrupcion de datos'

    await websocket.send(mensaje_servidor)

start_server = websockets.serve(main, host, 5092)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
