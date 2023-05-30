print(50*"=")
print("       PROGRAM MENAMBAH ISI LIST ")
print(50*"=")
nama = ['Asep', 'Ujang', 'Jajang']
# cara melihat seluruh isi pada List
print(nama)
print("")
# cara menambahkan data baru pada List(akan ditambahkan pada indeks terakhir)
nama.append('Iwan')
print("Hasil penambahan data pada List menggunakan method append")
print(nama)
print("")
# cara menambahkan data baru pada List dengan meletakannya sesuai index yang ditentukan
nama.insert(1, 'Bejo')
print("Hasil penambahan data pada List dengan menggunakan method insert")
print(nama)
print("")
# cara menambahkan data baru pada List dengan menggunakan method extend untuk memperluas jumlah element pada List
nama.extend(['Dadang', 'Iyan'])
print("Hasil penambahan data pada List dengan menggunakan method extend")
print(nama)
