# contoh penerapan tipe data Sets
# tipe data set mirip seperti himpunan
superhero = set({"a"})

# method add digunakan untuk menambahkan nilai kedalam sebuah variable
superhero.add("gundala")
superhero.add("wiro sableng")
superhero.add("saras 008")

# method sorted digunakan untuk mengurutkan data berdasarkan abjad pertama
# tipe data sets tidak bisa digunakan untuk memanggil nilai berdasarkan index tertentu,karena tipe data ini merupakan tipe data fixed
print(sorted(superhero))
print("")
# contoh implementasi kedua mengenai tipe data sets
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}
prima = {2, 3, 5, 7}

# method union untuk menggabungkan data pada tipe data sets
print(ganjil.union(genap))
# method intersection untuk mencari data yang kembar antara dua data yang dicocokan
print(ganjil.intersection(prima))
