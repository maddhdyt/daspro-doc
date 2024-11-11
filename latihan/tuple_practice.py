# Nama: Ahmad Hidayat
# NIM: 2410482
# Pertemuan: 3

# Tuple Append
myTuple = ("one", 2, "three", "four", 5, "six")

listChanger = list(myTuple)
listChanger.append("nana")
myTuple = tuple(listChanger)

print("Ini adalah append dalam tuple:", myTuple)

# Tuple Insert
listChanger = list(myTuple)
listChanger.insert(3, 3)
myTuple = tuple(listChanger)

print("Ini adalah insert dalam tuple:", myTuple)

# Tuple Pop
listChanger = list(myTuple)
listChanger.pop(2)
myTuple = tuple(listChanger)

print("Ini adalah pop dalam tuple:", myTuple)
