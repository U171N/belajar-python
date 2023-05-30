class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    #membuat method function didalam class Induk/parent class
    def showInfo(self):
        print("showinfo di class Hero")
        print("{} health: {}".format(self.name,self.health))
        
#membuat class turunan/inheritance
class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)
        
    #membuat overide method/menimpa function yang sudah ada didalam parent class kedalam inheritance atau class turunan
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(self.name, self.health))
        
class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name,200)
        
#membuat object untuk mengisi nilai terhadap variable yang didalam parent class yang telah ditimpa ke dlam class turunan atau inheritance
lina = Hero_intelligent('lina')

lina.showInfo() #menampilkan nilai yang ada didalam function showInfo yang ada di showInfo dari hasil overide atau menimpa suatu methode dari class parent
