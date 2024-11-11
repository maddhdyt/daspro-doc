# Nama: Ahmad Hidayat
# NIM: 2410482
# Kelas: RPL/1C

nilai = int(input("Masukan nilai ujian: "))

if nilai > 0:
    if nilai >= 90:
        grade = "A"
    elif nilai < 90 and nilai >= 80:
        grade = "B"
    elif nilai < 80 and nilai >= 70:
        grade = "C"
    elif nilai < 70:
        grade = "D"
    print(f"Grade nilai adalah {grade}")
elif nilai < 0:
    print("Nilai tidak valid")
