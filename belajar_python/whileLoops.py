# contoh penggunaan looping while dalam python
angka = 0
while angka < 5:
    print("nilai angka:", angka)
    angka = angka+1
print("print diluar while")


# contoh kedua
# start = True
# angka2 = 0

# while start:
#     print("didalam perulangan while")
#     if angka2 == 10:
#         start = False
#         print("angka 10 ditemukan")
#         angka2 += 1

# contoh ketiga menambahkan else kedalam looping while
angka3 = 0
while angka3 < 5:
    print("nilai angka:", angka3)
    angka3 += 1
else:
    print("nilai terakhir pada looping ini adalah:", angka3)

print(" ")
# contoh keempat menambahkan method break ke dalam looping while
angka4 = 0
while angka4 < 10:
    if angka4 == 5:
        break
    print("nilai angkanya adalah:", angka4)
    angka4 += 1
else:
    print("nilai angka terakhir adalah", angka4)

# contoh kelima menambahkan method continue ke dalam looping while
# angka5 = 0

# while angka5 < 10:
#     if angka5 == 5:
#         angka5 += 1  # menambahkan increment/iteration kedalam kondisi if untuk mencegah looping forever ketka menambahkan method continue
#         continue
#     print('nilai angka:', angka5)
#     angka += 1
# else:
#     print("nilai angka terakhir:", angka5)

# contoh keenam menambahkan method pass ke dalam looping while
angka6 = 0
while angka6 < 10:
    if angka6 == 5:
        pass
    print("nilai angka:", angka6)
    angka6 += 1
else:
    print("nilai angka terakhir:", angka6)
print("print diluar while")
