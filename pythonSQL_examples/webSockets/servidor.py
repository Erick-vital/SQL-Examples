import os
import asyncio
from cProfile import run
import websockets

async def handler(websocket):
    consulta = await websocket.recv()
    print(f'<<< {consulta}')

    if consulta == 'consulta':
        os.system('python3 consultas.py --order > ouputs.txt')
        os.system('python3 consultas.py --registros >> ouputs.txt')
        mensaje = 'el output de peticion a sido escrito en el archivo outputs.tx'
    else:
        mensaje = 'peticion no encontrada'

    # saludo = f'hola {consulta} !'

    await websocket.send(mensaje)
    print(f'>>> {mensaje}')

async def main():
    async with websockets.serve(handler, 'localhost', 8765):
        await asyncio.Future() # run forever

if __name__ == "__main__":
    asyncio.run(main())
    