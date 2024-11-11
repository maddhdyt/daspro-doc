# Nama: Ahmad Hidayat
# NIM: 2410482
# Prodi/Kelas: RPL/1C
# Pertemuan: 3

nilaiMahasiswa = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

total = sum(nilaiMahasiswa)
avarage = total / len(nilaiMahasiswa)
# A
print(f"nilai mahasiswa tertinggi: {max(nilaiMahasiswa)}")
print(f"nilai mahasiswa terendah: {min(nilaiMahasiswa)}")
print(f"nilai rata-rata mahasiswa: {avarage}")

# B
nilaiMahasiswa.sort()
nilaiMahasiswa.reverse()
print(f"nilai mahasiswa tertinggi kedua: {nilaiMahasiswa[1]}")
