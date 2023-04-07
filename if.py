# Inisialisasi variabel nilai dengan daftar nilai mahasiswa
nilai = [25, 90, 40, 95, 35, 70, 50, 20, 80, 65]

# Inisialisasi variabel terbesar dengan nilai terkecil yang mungkin
terbesar = 0

# Looping untuk mencari nilai terbesar
for n in nilai:
    if n > terbesar:
        terbesar = n

# Mencetak nilai terbesar
print("Nilai terbesar dari hasil ujian mahasiswa adalah:", terbesar)
