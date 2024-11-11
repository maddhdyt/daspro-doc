#Nama: Ahmad Hidayat
#NIM: 2410482
#Kelas: RPL / 1C

row = int(input("Masukan Jumlah Baris: "))
col = int(input("Masukan Jumlah Kolom: "))

total = 1

matrix = []

for i in range(row):
    ordo = []
    for j  in range(col):
        ordo.append(total)
        total += 1
    matrix.append(ordo)

for ordo in matrix:
    print(ordo)

    


