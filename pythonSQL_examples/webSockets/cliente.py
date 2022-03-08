import asyncio
import hashlib
import hmac
import urllib
import websockets
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os 

load_dotenv()

async def hello():
    url = 'ws://localhost:8765'
    async with websockets.connect(url) as websocket:
        private_key = input('Password: ')
        private_key = private_key.encode()
        TOKEN = '1234'

        parameters = {}
        parameters['token'] = TOKEN
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
