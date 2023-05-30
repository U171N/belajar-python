class Hero:
    
    #def__init__(self) adalah sebuah function constructor. Function ini akan dipanggil ketika object baru pertama kali di buat.
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name=inputName #kenapa menggunakan self karena attribut yang ditambahkan kedalam kelas sendiri(class Hero) bukan kelas lain
        self.health=inputHealth
        self.power=inputPower
        self.armor=inputArmor
        
hero1=Hero("Sniper",100,10,4) #memasukan nilai terhadap attribut yang ada didlam constructor __init__
hero2=Hero("mirana",100,15,1)
hero3=Hero("ucup",1000,100,0)

print(hero1.__dict__) #menampilkan semua attribut yang ada didalam object hero1 yang diambil dari constructor __init__
print(hero2.__dict__)
print(hero3.__dict__)