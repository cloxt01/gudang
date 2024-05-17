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

print("ID Acak dengan Format (idpertama8digit)-4digit-4digit-4digit-12digit:", random_custom_id)