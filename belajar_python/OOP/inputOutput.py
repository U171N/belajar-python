# contoh implementasi Input dan Output menggunakan python

# Cara membuat file

"""
Keterangan saat membuat file dengan menggunakan python

w= write mode/mode menulis dan menghapus file lama,jika file tidak ada maka akan membuat file baru
r= read only mode/hanya membaca isi file saja
a= appending mode/menambahkan data di akhir baris suatu file
r+ = write dan read mode

"""

file = open("test.txt", 'w')
file.write("contoh membuat file dengan menggunakan python")
file.write("\ntest")
file.close()


# cara membaca isi sebuah file dengan menggunakan python
bacaFile = open('test.txt', 'r')
# didalam read() ini bisa diisikan jumlah baris yang ingin ditampilkan/dibaca,contoh read(10) maka akan membaca 10baris dari suatu file
# print(bacaFile.read())

# cara membaca isi file berdasarkan baris yang dipilih
print(bacaFile.readline())

# appending mode/menambahkan isi kedalam suatu file
tambahData = open('test.txt', 'a')
tambahData.write('\ncontoh penambahan isi suatu file dengan python')
tambahData.close()
