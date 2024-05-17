import requests
import json
url = "https://access.kci.id/api/v1/gateway/access/user/kmt-card/getKMTCard"
data = {"card_number": "1003111902123721"}
headers = {
    "Host": "access.kci.id",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "User-Agent": "C-Access/4.2.80 (Android 12; M2004J19C; Redmi lancelot; in)",
    "Accept": "application/json",
    "Accept-Language": "in",
    "Cache-Control": "max-age=3",
    "Accept-Encoding": "gzip",
    "Content-Length": str(len(json.dumps(data)))
}


response = requests.post(url, headers=headers, json=data)

print(response.text)
