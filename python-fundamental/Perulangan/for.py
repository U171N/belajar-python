"""
syntax For=

for var in range(batas_awal,batas_akhir,step):
    pernyataan/statement
"""

print(50*"=")
print("Program deret Aritmatika")
print(50*"=")
sukuAwal = input("Masukan suku Awal = ")
beda = input("Masukan beda = ")
banyak = input("Masukan banyak deret = ")
jumlahDeret = int(banyak)+1
suku = int(sukuAwal)

for i in range(1, jumlahDeret, 1):
    print("Suku ke-", i, "=", suku)
    suku = suku+int(beda)
