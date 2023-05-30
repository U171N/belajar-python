judul = "PROGRAM MENGHITUNG PEMBELIAN"
print(judul.center(50, " "))
print(70*"=")
harga_satuan = int(input("Harga Satuan ="))
print("Rp", harga_satuan)
print("")
jml_pembelian = int(input("Jml Pembelian ="))
print("Jumlah =", jml_pembelian)
print("")
diskon = (harga_satuan*jml_pembelian)//100
print("HARGA diskon = Rp", diskon)
print("")
Harga_total = harga_satuan*jml_pembelian-diskon
print("Harga total = Rp", Harga_total)
