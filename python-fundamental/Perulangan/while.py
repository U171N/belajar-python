""" 
Syntax dasar perulangan while:

while kondisi:
    pernyataan perulangan/statement
"""

print(50*"=")
print("Program harga fotokopi per halaman")
print(50*"=")

lembar = 0
rp = 0
hrg = input("Masukan harga per lembar = ")
print("Daftar harga fotokopi @Rp ", hrg)
print("")

print(50*"=")
print("Lembar       Harga(Rp)")
print(50*"=")
while lembar < 5:
    lembar = lembar+1
    rp = rp+int(hrg)
    print(lembar, '          ', rp)
