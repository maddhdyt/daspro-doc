# Nama: Ahmad Hidayat
# NIM : 2410482
import datetime
from datetime import datetime

nama = input("Masukan nama anda: ")
tahunLahir = int(input("Masukan tahun lahir anda: "))
current_year = datetime.now().year
umur = current_year - tahunLahir

print(f"Halo Selamat datang {nama}! umur kamu adalah {umur}")
