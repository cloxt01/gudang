import asyncio
import websockets
import json
import uuid
import random
import string

# Fungsi untuk menghasilkan id acak dengan format tertentu
def generate_custom_id():
    # Membuat id pertama dengan 8 digit (kombinasi angka dan huruf)
    first_id_part = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # Membuat bagian-bagian berikutnya dari UUID
    rest_of_id = '-'.join(str(uuid.uuid4()).split('-')[1:])

    # Menggabungkan semua bagian
    custom_id = f"{first_id_part}-{rest_of_id}"

    return custom_id

# Menghasilkan ID acak dengan format yang diinginkan
random_custom_id = generate_custom_id()

async def send_and_receive_with_delay():
    uri = "wss://api.prod-us-west.realis.network/"
    try:
        async with websockets.connect(uri) as websocket:
            print("Terhubung ke server.")
            achievementKey = "32"
            # Loop tanpa henti untuk mengirim dan menerima data secara real-time
            while True:
            	
                  # Input yang akan dikirim
                  message = {"id":random_custom_id,"method":"lobby_achievementComplete","lang":"en","params":{"achievementKey": achievementKey,"userId":"UC95f60965"},"agent":"cats","auth":{"type":"mobileApp","deviceId":"745854038d8c42f3588b8589ee6e2549","appId":3}}
                  # Mengirim pesan ke server
                  #await websocket.send(json.dumps(message))

                  # Menerima respons dari server
                  #response = await websocket.recv()
                  #print(f"\nReceived response: {response}")
                  # Menunggu selama 1 detik
                  #await asyncio.sleep(1)
                  
                  #next = input("ENTER to continue")
                  #if next != '':
                  	#system("exit")
                 # print ("\r                                                           \r")
                  #message ={"id": random_custom_id,"method":"analytics_send","lang":"en","params":{"key":"achivements.gain","param":"key","value": achievementKey,"userId":"UC95f60965"},"agent":"analytics","auth":{"type":"mobileApp","deviceId":"745854038d8c42f3588b8589ee6e2549","appId":3}}
                  # Mengirim pesan ke server
                  await websocket.send(json.dumps(message))

                  # Menerima respons dari server
                  response = await websocket.recv()
                  print(f"\nReceived response: {response}")
                  # Menunggu selama 1 detik
                  #await asyncio.sleep(1)
                  
                  achievementKey = int(achievementKey)
                  achievementKey = str(achievementKey + 1)
                  #stop = input("ENTER to continue")
                  
    except websockets.exceptions.ConnectionClosedError:
        print("Koneksi ditutup oleh server atau gagal terhubung.")

asyncio.get_event_loop().run_until_complete(send_and_receive_with_delay())