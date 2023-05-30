# contoh function dengan menggunakan single parameter
def siswa(nama):
    print("siswa ini bernama", nama)


siswa('mario')
print("")
# contoh function dengan menggunakan double parameter


def guru(nama, pelajaran):
    print("guru ini bernama", nama)
    print("mengajar", pelajaran)


# membuat instansiasi object terhadap function dan memberikan nilai argument terhadap parameter
guru(nama='agus', pelajaran='matematika')
# contoh pemberian nilai argument terhadap parameter function yang salah(urutan mengasihkan nilai argument tidak pas)
guru('olah raga', 'eko')

print("")

# contoh implementasi function dengan default parameter


def penjagasekolah(nama, shift='siang', sifat='galak'):
    print("penjaga sekolah ini bernama:", nama)
    print("shiftnya:", shift)
    print("sifat:", sifat)


# membuat instansiasi object terhadap function dan memberikan nilai arguments
# memberikan nilai terhadap parameter yang blm memiliki default value
penjagasekolah("Entis")
penjagasekolah('Maman', shift='malam')
penjagasekolah('Asep', sifat='sangat galak')

# menghasilkan error,karena parameter nama blm ada nilai defaultnya tapi udh dibuat instansiasi object
# penjagasekolah(shift='malam', sifat="iya")
