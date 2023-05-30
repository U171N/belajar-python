nilai = 75
# contoh penggunaan kondisi if
if nilai == 75:
    print("nilainya:", nilai)

# contoh neested if
# hasil tidak muncul,dikarenakan if yang pertama bernilai false(yntuk bisa menampilkan hasil nested if tanpa operator logika spt and,or tidak akan tampil apa".Selain operator Logika bisa menambahkan operator math untuk memnuculkan hasilnya)
n1 = 80
n2 = 90
if n1 == 60:
    print("nilai saya:", n1)
    print("if pertama bernilai true")
    if n2 == 90:
        print("nilainya:", n2)
        print("if kedua bernilai true")

# contoh penggunaan ifelse

nilai = 80
print("====Contoh penggunaan If Else=====")
if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah D, lakukan perbaikan")
else:
    print("maaf anda tidak lulus kuliah ini")


# contoh penggunaan if else terhadap data list/array of object pada python
print(100*"+")
print(" ")
gorengan = ["bakwan", "cireng", "pisang goreng"]
# artinya variable list gorengan diasosiasikan oleh variable beli dan memanggil nilai list pada index ke.1
beli = gorengan[1]

if beli in gorengan:
    print('Mamang bilang, "ya, saya jual', beli, '"')
elif not beli in gorengan:
    print("sya tidak jual", beli)
else:
    print("tidak ada gorengan", beli)
