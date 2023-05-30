# contoh pertama implementasi Try and Exception

# while True:
#     try:
#         angka = int(input("masukan angka: "))
#         break
#     except:
#         print("yang anda masukan bukan angka")

# print("berhasil,anda memasukan angka: ", angka)
# print("")

# contoh kedua implementasi Try and Exception
while True:
    try:
        penyebut = int(input("masukan angka penyebut: "))
        pembilang = int(input("masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    # menggunakan exception terhadap nilai yang dimasukan(salah atau benar)
    except ValueError:
        print("yang anda masukan bukan angka\n")

    # menggunakan exception terhadap nilai yang salah(berupa angka 0)
    except ZeroDivisionError:
        print("mohon masukan angka selain 0(nol)")

    # menggunakan except dari program bawaan python yang menampilkan pesan errornya
    except Exception as error:
        print(error)

print("pembagian berhasil,hasilnya adalah: ", hasil)

"""
Tipe Error handling pada python:
1.IOError =digunakan untuk menangani inputan/Output yang dijalankan oleh user terhadap program
2.ImportError =digunakan untuk menangani ketika import module tapi tidak tersedia/belum terinstal
3.ValueError = digunakan untuk menangani ketika nilai yang dimasukan/di inputkan oleh user salah
4.DivisionError = digunakan untuk menangani ketika nilai yang dimasukan/diinputkan itu bernilai nol(0)/atau kosong
5.KeyboardInterupted
6.EOFError
"""
