class Hero:
    #ini contoh class variable
    jumlah=0
    
    #membuat constructor
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        #membuat instance variable
        self.name=inputName
        self.healt=inputHealth
        self.power=inputPower
        self.armor=inputArmor
        Hero.jumlah +=1
        print('membuat hero dengan nama ' +inputName)
        
#mmebuat object untuk class Hero dan menambahkan nilai untuk attribut constructornya
hero1=Hero("sniper",100,10,4)
print(Hero.jumlah)
hero2=Hero("juniper",100,20,5)
print(Hero.jumlah)