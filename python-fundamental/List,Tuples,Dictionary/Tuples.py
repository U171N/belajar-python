print(50*"=")
print("         Contoh pembuatan Tupple dengan nama tuppleKu")
print(50*"=")
tuppleKu = ("Hallo", 90, 45, "Selamat Siang", "Belajar")
print(tuppleKu)
print("")
print("Nilai indeks pada element 'Selamat Siang' = ", end="")
print(tuppleKu.index("Selamat Siang"))
print("")
print("Pengambilan sebuah elemen pada tuppleKu")
print("Isi tupple index ke-2 \t= ", tuppleKu[2])
print("Isi tupple index ke-3 \t= ", tuppleKu[3])
print("")
print("Slicing indeks 1 s.d index 2 = ", tuppleKu[1:3])
print("")
print("Iterasi terhadap tupple menggunakan looping: ")
for i in tuppleKu:
    print(i, end=" ")
print("\n===============================================")
