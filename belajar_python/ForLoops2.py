for i in range(10, 40, 5):  # artinya 10 adalah penambahan dimulai dari10 dan sampai 40.Dimana setiap penambahan bilangan tersebut ditambah 5
    print(i)

# menambahkan kondisi if didalam looping for
number = 25
# artinya perulangan dimulai dari angka 0-40 dan menggunakan increment otomatis yaitu 1.
for angka in range(0, 40):
    print(angka)
    if angka == 25:
        print('angka yang dicari=', angka, 'ditemukan')


# menambahkan break dan kondisi if else didalam looping for
number2 = 50
for angka2 in range(0, 40):
    print(angka2)

    if angka2 == number2:
        print('angka', angka2, 'ditemukan')
        break
else:
    # penempatan else harus sesuai dengan looping for,dikarenakan statement else ini digunakan untuk opsi lain pada looping for bkn statement kondisi if,jadi penempatannya harus mengikuti looping for.
    print('angka yang dicari tidak ditemukan')

print("diluar scope for looping")
