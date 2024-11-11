# Nama: Ahmad Hidayat
# NIM: 2410482
# Pertemuan: 3

# list buah
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(f"list buah saat ini: {buah}")
buah[2] = "cherry"

# mengganti ceri dengan cherry
print(f"list buah ceri yang diubah dengan cherry: {buah}")
print("AYO TAMBAHKAN BUAHMU SENDIRI!")
# input item oleh user
indexBuah = int(input("dimana index buah yang kamu inginkan:"))
buahUser = input("masukan buah yang ingin ditambahkan: ")

buah.insert(indexBuah, buahUser)
print(f"buah {indexBuah} telah ditambahkan: {buah}")

# sorting buah
buah.sort()
print(f"list buah yang telah disortir: {buah}")
