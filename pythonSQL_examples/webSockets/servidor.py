import os
from dotenv import load_dotenv
import hmac
import hashlib
import asyncio
from cProfile import run
import websockets

load_dotenv()
private_key = os.getenv('p_k').encode()

async def handler(websocket):
    mensaje = await websocket.recv()
    print(f'<<< {mensaje}')


    sign = hmac.new(private_key, mensaje, hashlib.sha256).hexdigest()

    await websocket.send(sign)
    #print(f'>>> {sign}')

async def main():
    async with websockets.serve(handler, 'localhost', 8765):
        await asyncio.Future() # run forever

if __name__ == "__main__":
    asyncio.run(main())
    