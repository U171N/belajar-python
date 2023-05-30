# Materi tentang classVariable pada python

# contoh pembuatan class python

class Mahasiswa():

    # membuat class variable
    jurusan = 'ekonomi'
    jumlah_mahasiswa = 0
    # membuat constructor __init__

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # attribute public
        self.nim = input_nim  # attribute public
        # menjumlahkan nilai argument instansiasi object
        Mahasiswa.jumlah_mahasiswa += 1


# membuat instansiasi object terhadap class Mahasiswa
otong = Mahasiswa('otong', 3301)
ucup = Mahasiswa('ucup', 3302)

# membuat class instansiasi object untuk menimpa/override nilai classVariable
otong.jurusan = 'sastra'

print(Mahasiswa.jurusan)
print(otong.jurusan)
print(ucup.jurusan)

print(Mahasiswa.__dict__)
# pada data jurusan yang ada diotong ini akan menimpa nilai default classVariable
print(otong.__dict__)
# menghitung counter nilai jumlah mahasiswa(ucup dan otong =2 mahasiswa)
print(Mahasiswa.jumlah_mahasiswa)

# catatan
# 1.attribute yang ada self nya maka itu bisa dibuat instansiasi object terhadap class dan menambahkan nilai argument didalamnya
# 2. attribute yang tidak ada self nya maka attribute itu hanya dimiliki oleh class dan tidak bisa di instansiasi object
