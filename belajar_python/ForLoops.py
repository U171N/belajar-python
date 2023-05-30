# list sebagai iterable
# iterable adalah objek yang memiliki iterator/properti dari objek yang menyediakan mekanisme untuk melintasi object
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

for g in gorengan:
    # g ini merupakan inisiasi variable baru yang merujuk terhadap variabel list gorengan
    print(g)
    print(len(g))  # untuk memasukan script/statement baru di looping,maka tempatnya harus sama ditengah/sama seperti statement sebelumnya

print(" ")
# membuat string sebagai iterable
bakwan = "bakwan"
for i in bakwan:
    print(i)

# membuat perulangan for didalam for/nested for

# 1.membuat list sebagai iterable terlebih dahulu
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

# 2.membuat function untuk memanggil seluruh list yang digunakan untuk iterable
Daftar_belanja = [gorengan, buah, sayur]
print(Daftar_belanja)

# 3.membuat for loop terhadap list nested yang dipanggil function Daftar_belanja
for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    # membuat nested for untuk memecah komponen terhadap parent for/looping for pertama
    for komponen in subDaftarBelanja:
        print(komponen)
