# Materi tentang teknik looping pada python

nama_band = ["D'Masiv",
             "Kangen Band",
             "Armada",
             "Dewa 19"]

kumpulan_lagu = ["Jangan menyerah",
                 "Bidadari",
                 "Mau dibawa Kemana",
                 "Arjuna"]

# menggunakan enumerate untuk menambahkan penghitungan index ke objek yang dilooping
for index, band in enumerate(nama_band):
    print(index, ':', band)  # artinya index  sebagai iterasi dengan menambahkan method enumerate untuk menghitung data berdasarkan index,dan band merupakan variable terhadap tanda :(titik dua) supaya lebih urut
print("")

# cara kedua penggunaan enumerate
for i in enumerate(nama_band):
    print(i, ":", nama_band)
print("")
# menggunakan zip untuk membentuk iterator berisi item/data pada tipe data list atau tipe data lainnya yanag kemudian digabungkan menjadi satu
for band, lagu in zip(nama_band, kumpulan_lagu):
    # penggunaan zip, data yang akan digabungkan harus memiliki jumlah yang sama/linear.Artinya misal variable A memiliki data 5 dan B memliki data 4,maka yang akan dibaca hanya 4 data dari kedua variable tersebut
    print(band, "membawakan lagu yang berjudul: ", lagu)
print("")
# contoh implemntasi looping terhadap tipe data set
playlist = {'baby baby', 'ada apa dengan cinta',
            'cenat-cenut', 'bukan superman'}
for lagu in sorted(playlist):
    print(lagu)
print("")
# contoh implementasi looping terhadap tipe data dictionary
musik = {
    'payung teduh': 'akad',
    'Fortwnty': 'Zona nyaman',
    'Dialog dini Hari': 'Rumahku'
}
# looping untuk mengambil data kunci terhadap dictionary
for i in musik.keys():
    print(i)
print("")
# looping untuk mengambil nilai dictionary
for i in musik.values():
    print(i)
print("")
# looping untuk mengambil semua data didalm dictionary
for i, music in musik.items():
    print(i, 'lagunya: ', music)
print("")
# looping dengan menambahkan method reverse
for i in reversed(range(1, 10, 1)):
    print(i)
