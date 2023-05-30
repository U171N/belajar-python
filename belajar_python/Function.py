# mendifinisikan sebuah function pada bahasa python
def function():
    print("contoh deklarasi function didalam python")


# cara memanggil function
function()

print("")
# contoh implementasi function pada bahasa python


def ayam():
    print("Contoh mencari harga ayam/Kg")


def hargaayam():
    ayam()
    print("harga ayam per 1kg adalah Rp.20.0000")

# membuat function dengan parameter dan untuk membuat callback function terhadap function diatasnya


def hargatotalayam(kg):
    ayam()
    harga = 20000
    hargatotal = kg*harga
    print("harga", kg, "ayam adalah", hargatotal)


# memberikan argument terhadap function diatas dan menginstasiasi function supaya bisa tampil
hargaayam()
hargatotalayam(2)
