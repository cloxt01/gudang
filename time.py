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


# Mendapatkan lima kursi
data_update = data_suara["ts"]
data_masuk = data_suara["chart"]["persen"]
hits = {
        "1": 1,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1,
        "7": 1,
        "8": 1,
        "9": 1,
        "10": 1,
        "11": 1,
        "12": 1,
        "13": 1,
        "14": 1,
        "15": 1,
        "16": 1,
        "17": 1,
        "24": 1
        }
data_partai = [
    "PKB",
    "GERINDRA",
    "PDIP",
    "GOLKAR",
    "NASDEM",
    "PB",
    "PGRI",
    "PKS",
    "PKN",
    "HANURA",
    "GERAIN",
    "PAN",
    "PBB",
    "DEMOKRAT",
    "PSI",
    "PERINDO",
    "PPP",
    "UMMAT"
]
lima_kursi = []
for i in range(10):
    # Mendapatkan kursimax
    kursi = int(max(data_suara["chart"], key=data_suara["chart"].get))
    partai_terpilih = str(kursi)
    kursi -= 1
    data_id = data_suara["table"][partai_terpilih]
    hits[partai_terpilih] += 2
    # Hapus variabel
    for partai, details in data_suara["table"].items():
        for key in ["jml_suara_total", "jml_suara_partai"]:
            details.pop(key, None)
    id_tertinggi = max(data_id, key=data_id.get)
    nama = data_identitas[partai_terpilih][id_tertinggi]["nama"]
    partai = data_partai[(int(partai_terpilih)-1)]
    nomor_urut = data_identitas[partai_terpilih][id_tertinggi]["nomor_urut"]
    tempat_tinggal = data_identitas[partai_terpilih][id_tertinggi]["tempat_tinggal"]
    suara_total = data_suara["chart"][partai_terpilih]
    suara = data_suara["table"][partai_terpilih][id_tertinggi]
    
    data_suara["chart"][partai_terpilih] /= hits[partai_terpilih]
    data_suara["table"][partai_terpilih].pop(id_tertinggi, None)
    
    # Menambahkan data ke lima_kursi
    lima_kursi.append({
        "kursi": i + 1,
        "id": id_tertinggi,
        "nama" : nama,
        "nomor_urut" : nomor_urut,
        "tempat_tinggal" : tempat_tinggal,
        "partai": partai,
        "suara": suara,
        "suara_total": suara_total
    })
    
    # Hapus data partai_terpilih untuk iterasi berikutnya
    

# Menghasilkan output lima kursi
lima_kursi_output = {i["kursi"]: {"id": i["id"], "nama": i["nama"], "nomor_urut": i["nomor_urut"], "tempat_tinggal": i["tempat_tinggal"], "partai": i["partai"], "suara": i["suara"], "suara_total": i["suara_total"]} for i in lima_kursi}
pretty_output_lima_kursi = json.dumps(lima_kursi_output, indent=4)
info = {
  "update" : data_update,
  "persen" : data_masuk
}
print(json.dumps(info, indent=4))
print(pretty_output_lima_kursi)
