import asyncio
import websockets
import json

async def send_and_receive_with_delay():
    uri = "wss://api.prod-us-west.realis.network/"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Terhubung ke server.")
            
            # Loop tanpa henti untuk mengirim dan menerima data secara real-time
            while True:
                email = input("email: ")

                # Input yang akan dikirim
                message = {"id": "84a60de-dd9a-452b-958e-da8a44b041f8", "method": "auth_createRequestToConfirmEmail", "lang": "en", "params": {"email": email, "referralCode": "UC95f60965"}, "agent": "auth", "auth": {"type": "mobileApp", "deviceId": "745854038d8c42f3588b8589ee6e2549", "appId": 3}}

                # Mengirim pesan ke server
                await websocket.send(json.dumps(message))

                # Menerima respons dari server
                response = await websocket.recv()
                print(f"Received response: {response}")

                # Menunggu selama 1 detik
                await asyncio.sleep(1)

                # Input yang akan dikirim setelah menerima respons
                user_input = input("Masukkan pesan (ketik 'exit' untuk keluar): ")
                if user_input.lower() == 'exit':
                    break

    except websockets.exceptions.ConnectionClosedError:
        print("Koneksi ditutup oleh server atau gagal terhubung.")

asyncio.get_event_loop().run_until_complete(send_and_receive_with_delay())