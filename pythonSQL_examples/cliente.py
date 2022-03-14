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

# Grupos de servidores
with open("gruposServidores.json", "r") as f:
    servidoresYgrupos = json.load(f)

# Variables de Entorno
load_dotenv()
private_key = os.getenv('p_k').encode()
token = os.getenv('token')
host = os.getenv('host')
port = os.getenv('port')

# Parametros
parameters = {}
parameters["token"] = token
parameters["timestamp"] = str(datetime.now().isoformat())

async def main():
    grupo_servidor = input('escribe el nombre o grupo de servidor: ')
    peticion = input('escribe tu peticion: ')
    if grupo_servidor in servidoresYgrupos['grupos']:
        grupo_servidor = servidoresYgrupos['grupos'][grupo_servidor]

        for servidor in grupo_servidor:
            ip = grupo_servidor[servidor]["ip"]
            puerto = grupo_servidor[servidor]["puerto"]
            async with websockets.connect(f"ws://{ip}:{puerto}") as ws:
                parameters["peticion"] = peticion
                mensaje = str(parameters)
                parameters["sign"] = hmac.new(private_key, mensaje.encode(), hashlib.sha256).hexdigest()
                await ws.send(pickle.dumps(json.dumps(parameters)))

                mensaje_del_servidor = await ws.recv()

                logging.info(mensaje_del_servidor)
                print(mensaje_del_servidor)




asyncio.get_event_loop().run_until_complete(main())