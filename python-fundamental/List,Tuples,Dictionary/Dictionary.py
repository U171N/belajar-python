dataKu = {"nim": "02826", "nama": "fakhruddin", "IPK": 3.50}
# Mencetak seluruh data Dictionary
print(dataKu)
print("")

# menampilkan salah satu nilai pada key didalam Dictionary
print(dataKu['nama'])
print("")

# menyimpan salah satu nilai pada kunci Dictionary ke variable lain
namaMhs = dataKu['nama']
print(namaMhs)
print("")

# cara akses satu nilai pada key Dictionary tanpa menampilkan sebuah pesan error
keterangan = dataKu.get('ket')
print(keterangan)
print("")

# akses satu nilai pada key Dictionary dan menyimpan ke variable lain tanpa menampilkan sebuah pesan error dengan nilai default yang akan dibuat
keterangan = dataKu.get('ket', 'lulus')
print(keterangan)
print("")

# mengetahui panjang pada Dictionary
print("Panjang data pada Dictionary dataKu = ", len(dataKu))
print("")

# mengetahui kunci"/key pada Dictionary dataKu
print(dataKu.keys())
print("")

# menampilkan nilai pada setiap key yang ada didalam Dictionary
print(dataKu.values())
print("")

# menampilkan setiap pasangan key dan values pada Dictionary
print(dataKu.items())
