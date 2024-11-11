# Nama: Ahmad Hidayat
# NIM: 2410482
# Kelas: RPL/1C

gender = input("Masukan gender anda: ")
age = int(input("Masukan umur anda: "))
height = int(input("Masukan tinggi badan anda: "))
iq = int(input("Masukan IQ anda: "))

if gender == "Pria" or gender == "Wanita":
    if gender == "Pria" and age >= 18 and age <= 25 and height >= 175 and iq >= 130:
        print(
            f"Selamat! Kualifikasi anda sesuai dengan syarat dan ketentuan untuk model dengan jenis kelamin {gender}"
        )
    elif gender == "Wanita" and age >= 18 and age <= 25 and height >= 170 and iq >= 130:
        print(
            f"Selamat! Kualifikasi anda sesuai dengan syarat dan ketentuan untuk model dengan jenis kelamin {gender}"
        )
    else:
        print("Maaf, kualifikasi anda tidak sesuai dengan syarat dan ketentuan")
else:
    print("Maaf, jenis kelamin harus Pria atau Wanita")
