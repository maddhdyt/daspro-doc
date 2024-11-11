# Nama: Ahmad Hidayat
# NIM: 2410482
# Kelas: RPL/1C

numberGroup = []
result = 0

while True:
    number = int(input("Input number: "))
    numberGroup.append(number)
    if number < 0:
        numberGroup.reverse()
        numberGroup.pop(0)
        break
result = sum(numberGroup)
print(f"total: {result}")
