import asyncio
import hashlib
import hmac
import urllib
import websockets
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os 

load_dotenv()

private_key = os.getenv('p_k').encode()
token = os.getenv('token')
async def hello():
    url = 'ws://localhost:8765'
    async with websockets.connect(url) as websocket:

        parameters = {}
        parameters['token'] = token
        parameters['timestamp'] = str(datetime.now().isoformat())

        mensaje = str(parameters.items()).encode()

        actual_digest = hmac.new(private_key, mensaje, hashlib.sha256).hexdigest()
        print(f'>>> actual_di: {actual_digest}')

        await websocket.send(mensaje)

        sign = await websocket.recv()
        if hmac.compare_digest(actual_digest, sign):
            print('todo correcto')
        else:
            print('PELIGRO: posible corrupcion de datos')
        print(f'<<<  recibido: {sign}')
if __name__ == '__main__':
    asyncio.run(hello())
