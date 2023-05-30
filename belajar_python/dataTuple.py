# tipe data list
import sys
import timeit
Ganjil = [1, 3, 5]

# tipe data tuple
Genap = (2, 4, 6)

# mengecek tipe data diatas
print(type(Ganjil))
print(type(Genap))

# mengecek method apa saja yang bisa dipakai untuk data tuple
print(dir(Genap))
print(100*"+")

# melihat perbedaan ukuran antara tipe data list dan tuple

data_list = [1, 2, 3, 4, 5, "pisang goreng", "via vallen", False, 3.14]
data_tuple = (1, 2, 3, 4, 5, "pisang goreng", "via vallen", False, 3.14)

# mengecek besar ukuran data list dan data tuple
besar_dataList = sys.getsizeof(data_list)
besar_dataTuple = sys.getsizeof(data_tuple)

print("besar data list: ", besar_dataList)
print("besar data tuple: ", besar_dataTuple)
print("")
# mengecek waktu proses compile antara data list dan data tuple
time_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=10000)
time_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=10000)

print("waktu runtime untuk compile data List sebesar: ", time_list)
print("waktu runtime compile data Tuple sebesar: ", time_tuple)

# Catatan
# 1.ketika ingin menggunakan tipe data untuk diubah-ubah nilainya maka gunakan tipe data List
# 2.ketika ingin menggunkana tipe data yang fixed tanpa perlu diubah-ubah nilainya dan mempercepat proses runtime data bisa gunakan tipe data Tuple
