
#membuat class induk/parent class
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    #membuat method function untuk mengambil data dari parameter constructor
    def showInfo(self):
        print("{} dengan health: {}".format(self.name, self.health))
        
#membuat class turunan dari class induk
class Hero_intelligent(Hero):
    def __init__(self,name):
        #menggunakan super untuk menampilkan data dari class Induk
        super().__init__(name,100)
        super().showInfo()
        
class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)
        super().showInfo()

#membuat object dari class induk/parent class
lina = Hero_intelligent('lina')
axe = Hero_strength('axe')