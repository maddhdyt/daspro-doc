# Nama: Ahmad Hidayat
# NIM: 2410482
# Kelas: RPL/1C

jumlahBarang = int(input("masukan jumlah barang: "))
harga = 0
if jumlahBarang > 0:
    if jumlahBarang < 100:
        harga = 5000
    elif jumlahBarang >= 100 and jumlahBarang <= 150:
        harga = 4000
    elif jumlahBarang > 150:
        harga = 2500
totalHarga = jumlahBarang * harga
print(f"jumlah barang adalah {jumlahBarang}")
print(f"harga per barang adalah Rp.{harga}")
print(f"total harga barang adalah Rp.{totalHarga}")
