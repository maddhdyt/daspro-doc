#Nama: Ahmad Hidayat
#NIM: 2410482
#Kelas: RPL 1C

#Nabila's Online Shop
shopCatalog = ["T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok", "Baju Renang", "Tas", "Topi", "Sepatu", "Sendal"]
print("Berikut list product Nabila's Shop pada bulan Juli:")
print(shopCatalog)
print("Berjumlah", len(shopCatalog))

shopCatalog[5] = "Gamis"
shopCatalog.extend(["Ikat Rambut", "Kerudung"])
print("Berikut list product Nabila's Shop pada bulan Agustus:")
print(shopCatalog)
print("Berjumlah", len(shopCatalog))