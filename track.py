import requests

def lacak_lokasi_ip_matrix(ip_target):
    url = f"http://ip-api.com/json/{ip_target}"
    response = requests.get(url)
    
    if response.status_code == 200:
        informasi_lokasi = response.json()
        return informasi_lokasi
    else:
        return "Gagal mengakses layanan geolokasi."

def rapihkan_respons(respons):
    if isinstance(respons, str):
        return respons  # Jika respons adalah string, kembalikan tanpa merapikan
    hasil_rapih = "\n".join([f"{k}: {v}" for k, v in respons.items()])
    return hasil_rapih

def buat_link_google_maps(lat, lon):
    return f"https://www.google.com/maps/place/{lat},{lon}"

# Contoh penggunaan
ip_target = input("IP address: ")
hasil_pelacakan = lacak_lokasi_ip_matrix(ip_target)

if isinstance(hasil_pelacakan, dict):
    hasil_rapih = rapihkan_respons(hasil_pelacakan)
    print(hasil_rapih)

    # Ambil latitude dan longitude dari respons
    lat = hasil_pelacakan.get('lat', '')
    lon = hasil_pelacakan.get('lon', '')

    if lat and lon:
        link_google_maps = buat_link_google_maps(lat, lon)
        print(f"Link Google Maps: {link_google_maps}")
    else:
        print("Tidak dapat menemukan informasi latitude dan longitude.")
else:
    print(hasil_pelacakan)