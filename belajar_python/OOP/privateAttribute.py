class Mahasiswa():
    # membuat propertie dengan visibilty atau hak akses public
    # jurusan='teknk mesin'

    # membuat propertie dengan visibilty atau hak akses private
    # untuk mengakses properti private ini harus diubah kedalam scope local didalam method function yang masih satu class
    __nilai = 0

    # membuat constructor __init__
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # propertie public
        self.nim = input_nim  # propertie public

    # membuat method function
    def uts(self, input_nilai):
        # memasukan propertie didalam sebuah method function supaya bisa ditampilkan nilai/datanya
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        # memasukan propertie didalam sebuah method function supaya bisa ditampilkan
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'tidak lulus')
        else:
            print(self.nama, 'lulus')


# membuat instansiasi object dengan memberikan nilai arugment terhadap constructor __init__
otong = Mahasiswa('otong surotong', 3328)
print(otong)

otong.uts(50)
otong.uas(70)
otong.check_status()
