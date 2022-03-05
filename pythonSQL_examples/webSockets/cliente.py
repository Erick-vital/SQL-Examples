import asyncio
import websockets

async def hello():
    url = 'ws://localhost:8765'
    async with websockets.connect(url) as websocket:
        consultas = input('escribe tu peticion: ')

        await websocket.send(consultas)
        print(f' >>> {consultas}')

        saludo = await websocket.recv()
        print(f'<<< {saludo}')

if __name__ == '__main__':
    asyncio.run(hello())
