class Mangga:
    
    #membuat constructor
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah
        
    #membuat sebuah magic method

    #Fungsi repr() berfungsi untuk mengembalikan representasi dari suatu objek.Biasanya ini digunakan sebelum nilai atau parameternya digunakan atau dipanggil
    def __repr__(self):
        return "Mangg: {} dengan jumlah: {}".format(self.nama, self.jumlah)
    
    #Fungsi __str__ dalam Python hanya digunakan untuk mengembalikan output dari fungsi Python dalam format string.
    def __str__(self):
        return "Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    #Method __add__ mengizinkan operator + pada class.
    def __add__(self, object):
        return self.jumlah + object.jumlah

belanja1 = Mangga("arumanis",10)
belanja2 = Mangga("mana lagi",5)
print(belanja1)
print(belanja2)
#mencetak fungsi overloading __add__
print(belanja1 + belanja2)

#menampilkna data didalam class berupa dictionary
print(belanja1.__dict__)