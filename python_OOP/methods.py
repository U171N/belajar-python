class Hero: #membuat template class
    jumlah_hero=0
    
    #membuat constructor
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        
    #membuat void function/method tanpa return
    def siapa(self):
        print("namaku adalah " + self.name) #ini akan menampilkan nilai pada instance variable yang merujuk pada parameter constructor diatas
        
    #membuat void function/method dengan argumen
    def healthUp(self,up):
        self.health += up #ini akan mengubah nilai default dari atribute yang sdh dibuat didalam object hero1
           
    #membuat void function/method dengan return
    def getHealth(self):
        return self.health #ini akan mengembalikan nilai dari atribute yg sudah diubah nilai dengan menggunakan function healtUp sebelumnya/diatasnya
        
#membuat object yang merujuk class tsb
hero1=Hero('sniper',100,10,5)
hero2=Hero('mario bros',90,5,10)

hero1.siapa()

#mengubah nilai default yang ada pada atribute instance variable
hero1.healthUp(10)

#menampilkan nilai pada atribute instance variable yang sudah dilakuakn return
print(hero1.getHealth())