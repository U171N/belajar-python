# penerapan scope variable:local

namaKucing = 'cassandra'
makananKucing = 'royal canin'


def ubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print("nama kucing yang baru adalah:", namaKucing)

# contoh penerapan variable scope  global


def kasihMakan(makanan, nama):
    global namaKucing, makananKucing
    namaKucing = nama
    makananKucing = makanan


# instansiasi objek dengan menambahkan sebuah nilai argument untuk sebuah parameter function
ubahNamaKucing('Tom')

# contoh instansiasi objek dengan menambahkan sebuah nilai argument pada variable scope global

# nilai cassandra(default value variable) akan diganti oleh nilai baru
kasihMakan('universal', 'alex')
print('nama kucingnya sebelumnya:', namaKucing, 'dan makan', makananKucing)
