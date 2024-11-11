#Nama: Ahmad Hidayat
#NIM: 2410482
#Kelas: RPL 1C

wallPrice = 520000
length = 8
height = 4
width = 10

calculateWallWide = 2 * (length * height) + 2 * (width * height)
calculatePrice = int(calculateWallWide * wallPrice)

print(f"Total luas dinding adalah {calculateWallWide} m2")
print(f"Total biaya yang Pak Abi harus keluarkan adalah RP{calculatePrice}")
