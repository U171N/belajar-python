# contoh implementasi inheritance/pewarisan didalam python

class Ojek():

    # membuat construct __init__
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    # membuat method function
    def cek_id_ojek(self):
        print('nama:', self.nama, '\nmotor:',
              self.transmisi, '\ndaerah:', self.daerah)

# membuat inheritance/turunan class Ojek


class Gojek(Ojek):
    def cek_id_ojek(self):
        print('contoh method function didalam inheritance')


# membuat instansiasi object terhadap class dan memberikan nilai argument
ojek1 = Ojek('mario', 'kopling', 'jakarta')
# ini tidak akan tampil karena method function yang ada diclass utama/parent class sudah ditimpa atau mengalami overide didalam class inheritance Gojek
ojek2 = Gojek('teguh', 'matic', 'bandung')

# mencetak nilai dari argument diatas
ojek1.cek_id_ojek()
ojek2.cek_id_ojek()
