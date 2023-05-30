#latihan ini digunakan untuk mengetahui ketika fungsi pada python mengeksekusi programnya maka nilainya akan diurutkan berdasarkan parameter yang ada dan ini sesuai urutannya
def urutanParameter(a1,a2,a3):
    print("Bil-1 = ",a1)
    print("Bil-2 = ",a2)
    print("Bil-3 = ",a3)
    hasil=a1+a2+a3
    return hasil

hasil = urutanParameter(a2=10,a3=7,a1=3)
print(hasil)
