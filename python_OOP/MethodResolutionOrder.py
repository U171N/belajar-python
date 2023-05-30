#membuat parent class pertama
class A:
    
    #membuat method function parent class A
    def show(self):
        print("ini adalah contoh method function A")
        
#membuat parent class kedua
class B:
    
    #membuat method function parent class B
    def show(self):
        print("ini adalah contoh method function B")
        
#membuat multiple inherintance terhadap parent class A dan B
class C(A,B):
    
    #membuat method function untuk class inherintance C
    # def show(self):
    #     print("ini adalah contoh method function C")

    #menambahkan property pass untuk menyembunyikan semua attribute yang ada diclass C ini
    pass
        
    
#membuat object untuk menampilkan data apa saja yang ada didalam class inheritance C
object = C()
object.show()

#menampilkan urutan data yang dipanggil dari masing"class yang ada
# help(object) ->ketika menambahkan property pass didalam suatu class maka otomatis data yang tampil adalah data yang ada di class sebelumnya
