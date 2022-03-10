import os
from dotenv import load_dotenv
import asyncio
from cProfile import run
import websockets
from claseAbstracta import Consultas

load_dotenv()

private_key = os.getenv('p_k').encode()
host = os.getenv('host')
port = os.getenv('port')

async def main(websocket, path):
    mensaje = await websocket.recv()
    c = Consultas(mensaje)

    mensaje_servidor = c.run()

    await websocket.send(mensaje_servidor)

start_server = websockets.serve(main, host, port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

