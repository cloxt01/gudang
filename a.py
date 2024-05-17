import requests
import json

url_nama = "https://sirekap-obj-data.kpu.go.id/pemilu/caleg/partai/360204.json"
url_jumlah = "https://sirekap-obj-data.kpu.go.id/pemilu/hhcd/pdprdk/36/3602/360204.json"

headers = {
    "Host": "sirekap-obj-data.kpu.go.id",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://pemilu2024.kpu.go.id",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://pemilu2024.kpu.go.id/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

# Get data for 'nama'
respon_nama = requests.get(url_nama, headers=headers)
data_identitas = respon_nama.json()
with open('respon_nama.txt', 'w') as file:
    file.write(respon_nama.text)

# Get data for 'jumlah'
respon_jumlah = requests.get(url_jumlah, headers=headers)
data_suara = respon_jumlah.json()
with open('respon_jumlah.txt', 'w') as file:
    file.write(respon_jumlah.text)

# Mendapatkan kursi pertama
kursi_pertama = max(data_suara["chart"], key=data_suara["chart"].get)

# Mendapatkan partai terpilih
partai_terpilih = str(kursi_pertama)

# Hapus variabel
for partai, details in data_suara["table"].items():
    for key in ["jml_suara_total", "jml_suara_partai"]:
        details.pop(key, None)

# Mendapatkan ID dari suara tertinggi pada partai terpilih
id_tertinggi = max(data_suara["table"][partai_terpilih], key=data_suara["table"][partai_terpilih].get)

# Menghasilkan output yang diinginkan
lima_kursi = {}

# Fungsi untuk mendapatkan kursi berdasarkan peraturan yang dijelaskan
def dapatkan_kursi(nomor_kursi):
    nonlocal data_suara
    nonlocal partai_terpilih
    nonlocal id_tertinggi
    nonlocal lima_kursi

    for _ in range(nomor_kursi):
        # Mendapatkan kursi
        kursi = {
            "partai": partai_terpilih,
            "id": id_tertinggi,
            "suara": data_suara["table"][kursi_pertama][id_tertinggi]
        }

        # Menambahkan kursi ke dalam hasil
        lima_kursi[len(lima_kursi) + 1] = kursi

        # Menghapus suara partai terpilih dari chart
        data_suara["chart"].pop(partai_terpilih, None)

        # Mendapatkan partai terpilih yang baru
        partai_terpilih = str(max(data_suara["chart"], key=data_suara["chart"].get))

        # Hapus variabel yang tidak diperlukan
        for partai, details in data_suara["table"].items():
            for key in ["jml_suara_total", "jml_suara_partai"]:
                details.pop(key, None)

        # Mendapatkan ID dengan suara tertinggi pada partai terpilih yang baru
        id_tertinggi = max(data_suara["table"][partai_terpilih], key=data_suara["table"][partai_terpilih].get)

        # Dibagi +2 dari nilai sebelumnya untuk partai yang terpilih pada pemilihan kursi berikutnya
        for partai, details in data_suara["table"].items():
            if partai != partai_terpilih:
                details["jml_suara_total"] /= 2

# Mendapatkan lima kursi berdasarkan peraturan yang dijelaskan
dapatkan_kursi(5)

# Mencetak hasil
pretty_output = json.dumps(lima_kursi, indent=4)
print(pretty_output)
