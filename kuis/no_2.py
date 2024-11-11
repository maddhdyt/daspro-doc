#Nama: Ahmad Hidayat
#NIM: 2410482
#Kelas: RPL 1C

fieldLength = int(input("Masukan Panjang Lapangan: "))
fieldWidth = int(input("Masukan Lebar Lapangan: "))

oneRound = fieldLength + fieldWidth * 2

runningDistance = int(input("Masukan jarak berlari(km): "))

totalRound = oneRound * runningDistance

convertToKm = totalRound / 1000

print(f"Jarak yang ditempuh Bu Rinda yaitu {convertToKm} Km")