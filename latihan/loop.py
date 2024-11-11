# Nama  Ahmad Hidayat
# NIM = 2410482
# Kelas = RPL/1C

batas = int(input("Masukkan batas angka: "))
print(f"Deret angka 1-{batas} (kelipatan 5 diganti 'pass'):")

for angka in range(1, batas + 1):
    if angka % 5 == 0:
        print("pass")
    else:
        print(angka)