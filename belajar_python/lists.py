Data = [1, 4, 9, 16, 25, 36, 49, 64]
print(Data)

subdata = Data[0]  # memanggil data pada array of object dengan index ke.0
print(subdata)

subdata2 = Data[-3]
print(subdata2)

# artinya nilai yang dipanggil itu sampe nilai sebelum urutan index ke.4/sampe index ke.3.Dalam artian nilai yang dipanggil mulai dari index ke.0-3
subdata3 = Data[0:4]
print(subdata3)

# artinya memanggil nilai mulai dari index ke.0 secara otomatis
subdata4 = Data[:4]
print(subdata4)

# artinya memanggil nilai mulai dari index ke.6 sampe index selanjutnya secara otomatis
subdata5 = Data[6:]
print(subdata5)

Data2 = [100, 200, 300, 400, 500, 600, 700, 800]
# menambahkan list Data1 dan Data2
Data3 = Data+Data2
print(Data3)

# merubah isi/nilai pada list
print(Data)
# Data[4] = 87  # merubah nilai pada index ke.4 yaitu 25 menjadi 87

a = Data[:]  # tanda : artinya menyalin semua nilai yang ada didalam variable Data ke dalam Variable a yang telah di asosiasikan
a[4] = 87
print(a)

# merubah nilai list variable Data dengan menggunakan methode slicing
Data[3:5] = [11, 12]
print(Data)

# list dalam list
x = [Data, Data2]

# mengakses list dalam multidimensional list
# artinya memanggil Data yang pertama(Data2) dengan nilai index ke.4 pada list Data2
y = x[1][4]

print(x)
print(y)

# method untuk menambahkan attribute ke dalam list/method untuk list pada bahasa python
Data.append(Data2)
print(Data)

Data.append(30)  # menambahkan nilai baru didalam list
print(Data)

# menambahkan function ke dalam list
# artinya membuat function dengan nama panjang_list dan menggunakan method len untuk mengetahui karakter pada list Data
panjang_list = len(Data)
print(Data)
print(panjang_list)
