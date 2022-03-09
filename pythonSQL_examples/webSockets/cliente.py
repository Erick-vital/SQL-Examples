import asyncio
import hashlib
import hmac
import json
import logging
import websockets
from datetime import datetime
from dotenv import load_dotenv
import os 
import pickle
import json

load_dotenv()

private_key = os.getenv('p_k').encode()
token = os.getenv('token')
host = os.getenv('host')
port = os.getenv('port')

parameters = {}
parameters["token"] = token
parameters["timestamp"] = str(datetime.now().isoformat())

async def main():
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        peticion = input('escribe tu peticion: ')
        parameters["peticion"] = peticion
        mensaje = str(parameters)
        parameters["sign"] = hmac.new(private_key, mensaje.encode(), hashlib.sha256).hexdigest()
        await ws.send(pickle.dumps(json.dumps(parameters)))

        mensaje_del_servidor = await ws.recv()

        logging.info(mensaje_del_servidor)
        print(mensaje_del_servidor)


asyncio.get_event_loop().run_until_complete(main())
