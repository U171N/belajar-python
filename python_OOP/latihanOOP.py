class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name=name
        self.health=health
        self.attackPower=attackPower
        self.armorNumber=armorNumber #armorNumber ataupun semua yang dicantumkan setelah = itu merupakan pemanggilan dari parameter constructor class Hero
    

    #membuat method function serang
    def serang(self,lawan): #disini selain memasukan self yang menyatakan class itu sendiri,kita bisa memasukan paramter lainnya,yang terpenting didalam
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self,self.attackPower)
    #membuat method function diserang
    def diserang(self,lawan,attackPower_lawan):
        print(self.name + ' diserang ' +lawan.name)
        attack_diterima= attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah' + self.name + ' tersisa ' + str(self.health))

#membuat object untuk class Hero dan memasukan nilai setiap parameter nilai dari class Hero yang ada diconstructor
sniper=Hero('sniper',100,10,5)
rikimaru=Hero('rikimaru',100,50,20)

sniper.serang(rikimaru) #dikarenakan disini pada method serang yang dipanggil object rikimaru,otomatis method function diserang berkebalikan dari pemanggilan object pada method function serang
print("\n")
rikimaru.serang(sniper)
print("\n")