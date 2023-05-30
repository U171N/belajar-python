class Hero:
    
    #membuat constructor
    def __init__(self,name,health,attackPower):
        self.__name=name
        self.__health=health
        self.__attPower=attackPower
        
    #membuat method getter untuk mendapatkan nilai dari sebuah parameter yg diambil dari constructor yang dimasukin didalamnya
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    #membuat method setter untuk mengatur sebuah nilai baru dan bisa menambahkan attribute atau parameter baru agar bisa dipanggil oleh object class
    def diserang(self,serangPower):
        self.__health -= serangPower
        
#membuat object dan memberi nilai terhadap parameter yang ada
earthshake = Hero("earthshake",50,5)

#menampilkan dari setiap data yang ada
print(earthshake.getName())
print(earthshake.getHealth())
earthshake.diserang(5)
print(earthshake.getHealth())