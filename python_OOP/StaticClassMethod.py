class Hero:
    
    #membuat privat class Variable
    __jumlah = 0
    
    #membuat sebuah constructor
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah +=1
        
    #membuat sebuah method getter
    def getJumlah(self):
        return Hero.__jumlah
    
    #membuat sebuah method getter untuk object tp tdk berlaku untuk class(Hero)
    def getJumlah1():
        return Hero.__jumlah
    
    #membuat static method(decorator) yang bisa nempel ke object(disini contohnya:sniper,dan rikimaru) dan class(Hero)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    #membuat class method
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

#membuat object1 dan memasukan nilai pada parameter nama
sniper=Hero('sniper')
print(Hero.getJumlah2()) #mencetak nilai yang ada dari class Hero menggunakan static method

#membuat object2
rikimaru=Hero('rikimaru') #memberikan nilai terhadap parameter/attribute constructor yang ada didalam class Hero
print(rikimaru.getJumlah2()) #mencetak nilai yang ada dari class Hero menggunakan static method dan ini akan otomatis bertambah dari 1 ke 2,karena properti yang dipanggil menggunakan increment

#membuat object3 untuk test classmethod
drowranger=Hero('drowranger')
print(drowranger.getJumlah3())


"""
Kesimpulan:

Jika static method tdk bisa menggunakan argument/paramater,namun classmethod bisa ditambahkan argument/paramater
"""