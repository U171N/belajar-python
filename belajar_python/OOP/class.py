# Contoh penerapan OOP pada python

# implmentasi class pada python
class Mahasiswa():

    # contoh penerapan constructor atau __init__ pada python
    # fungsi dari __init__ pada python untuk konfigurasi object yang telah di-construct. Pada __init__ function umumnya dilakukan inisialisasi properties, atau melakukan operasi yang harus dilakukan sebelum object dibuat
    def __init__(self, input_nama):
        self.nama = input_nama

        # membuat method function
    # Fungsi dari “self” ini sebenarnya adalah sebagai sebuah variabel saja yang yang menyatakan kelas itu sendiri.
    # method function harus didalam satu block/indent class

    def belajar(self, kondisi):
        print(self.nama, 'ini contoh method function oop pada python', kondisi)


# membuat instance object terhadap class Mahasiswa
# test merupakan instance atau instansiasi objectnya
# test = Mahasiswa('farudin')
# memberikan nilai argument untuk menajalankan fungsi __init__
uji = Mahasiswa('farudin')

# # mengganti default value statment function
uji.nama = 'bedul'
# print(test)

# # uji instance object class Mahasiswa ke.2
# print(test.nama)
print(uji.nama)

# membuat instance object terhadap method function
# menambahkan nilai argument untuk parameter yang ada
uji.belajar('latihan oop python')
