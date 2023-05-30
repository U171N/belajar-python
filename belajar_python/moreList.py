# Materi tentang List

# mendefinisikan list
barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']
print(barang)

# beberapa method yang digunakan dalam penggunaan list

# 1.method appned(untuk menambahkan object kedalam sebuah list)
barang.append('sepeda')
print(barang)

# 2.method extend(untuk menambahkan data list kedalam sebuah list lainnya).Setiap karakter memiliki index sendiri"
barang.extend('dompet')
print(barang)

# 3.method insert(digunakan untuk memasukan sebuah object kedalam index yang telah ditentukan)
# artinya 3 adalah urutan index nilai yang telah ditentukan,kemudian diikuti nilai baru yang akan dimasukan ke dalam list
barang.insert(3, 'sepeda')
print(barang)

# 4.method count(untuk menghitung anggota yang ada didalam list)
jumlahSepeda = barang.count('sepeda')
print("jumlah sepeda yang ada didalam list ada:", jumlahSepeda)

# 5.method remove(untuk menghapus data)
barang.remove('sepeda')
print(barang)

# 6.method reverse(untuk membalik urutan object yang ada didalam list)
barang.reverse()
print(barang)

print("")
# 6.method copy(untuk menyalin data object list lama dan tidak menimpa data list lama)
baru = barang.copy()
baru.append('gelas')
print(baru)
print(barang)
