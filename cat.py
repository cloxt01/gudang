import asyncio
import websockets
import json

async def receive_and_display(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(f"Received response: {response}")
        except websockets.ConnectionClosed:
            print("Koneksi ditutup oleh server.")
            break

async def send_user_input(websocket):
    while True:
        user_input = input("\nMasukkan pesan (ketik 'exit' untuk keluar): ")
        
        if user_input.lower() == 'exit':
            break
        
        message = {"input": user_input}
        await websocket.send(json.dumps(message))

async def main():
    uri = "wss://api.prod-us-west.realis.network/"

    try:
        async with websockets.connect(uri) as websocket:
            print("\nTerhubung ke server.")
            
            # Membuat dua tugas asinkron bersamaan
            receive_task = asyncio.create_task(receive_and_display(websocket))
            send_task = asyncio.create_task(send_user_input(websocket))

            # Menunggu hingga salah satu tugas selesai
            await asyncio.gather(receive_task, send_task)

    except websockets.exceptions.ConnectionClosedError:
        print("Gagal terhubung ke server.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())