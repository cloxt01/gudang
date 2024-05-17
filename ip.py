import requests

def cek_ip_address_publik():
    try:
        response = requests.get('https://httpbin.org/ip')
        ip_address = response.json()['origin']
        return f"IP address publik Anda: {ip_address}"
    except requests.RequestException as e:
        return f"Tidak dapat mendapatkan IP address publik. Kesalahan: {e}"

# Contoh penggunaan
hasil_cek_ip_publik = cek_ip_address_publik()
print(hasil_cek_ip_publik)