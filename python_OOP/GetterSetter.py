class Hero:

    #membuat constructor
    def __init__(self,name,health,armor):
        self.name = name #untuk membuat attribute ini menjadi variable dinamis maka hak akses diubah dari private atau __namavariable menjadi data public
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)

    #membuat property untuk mengubah sebuah method menjadi sebuah variable biasa
    #@property ini akan mengubah sebuah variable static menjadi dinamis artinya ketika nilainya berubah maka ketika dipanggil jg akan berubah
    @property
    #memasukan attribute yang ada didalam constructor kedalam method info
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)

    #membuat method setter
    @property
    def armor(self):
        pass #pass disini digunakan agar nilai yang ada bisa dipanggil di method getter nantinya

    @armor.getter #untuk membuat method getter maka kita harus memanggil nama method setter nya terlebih dahulu
    def armor(self):
        return self.__armor

    #membuat method setter untuk menginputkan nilai pada variable
    @armor.setter
    def armor(self,input):
        self.__armor = input

    #membuat method deleter untuk menghapus data pada variable yang sudah tdk dipakai
    @armor.deleter
    def armor(self):
        print('data armor dihapus')
        self.__armor = None
#membuat object untuk class Hero dengan nama sniper
sniper=Hero('sniper',100,10)
print(sniper.info)

#mengubah nilai sebuah attribute yang ada di @property
sniper.name ='dadang'
print(sniper.info)

#menampilkan hasil setter dan getter
print('contoh getter dan setter pada python:')
#menampilkan nilai pada default sebuah variable
print(sniper.armor)
print(sniper.__dict__)

#mengubah nilai pada variable armor yang ada di method setter
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)


#menghapus data
print("hapus data armor")
del sniper.armor
print(sniper.__dict__)