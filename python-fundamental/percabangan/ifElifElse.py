print("Program Menghitung Luas bidang sederhana")
print(50*"=")
print("1 Menghitung Luas Persegji Panjang")
print("2 Menghitung Luas Lingkaran")
print("3 Menghitung Luas Segitiga \n")
pilih = input("Masukan Pilihan (1-3): ")
print("\n")

if int(pilih) == 1:
    print("Menghitung Luas Persegi Panjang \n")
    p = input("panjang =")
    l = input("Lebar =")
    luas = float(p)*float(l)
    print("Luas = ", luas)

elif int(pilih) == 2:
    print("Menghitung Luas Lingkaran \n")
    r = input("Jari-jari = ")
    luas = 3.14 * float(r)*float(r)
    print("Luas lingkaran =", luas)

elif int(pilih) == 3:
    print("Menghitung luas Segitiga =")
    a = input("alas =")
    t = input("Tinggi =")
    luas = 0.5*float(a)*float(t)
    print("Luas Segitiga=", luas)

else:
    print("anda memasukan angka yang salah")
