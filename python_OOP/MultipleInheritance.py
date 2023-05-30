#membuat parent class pertama
class Team:
    #membuat method function didalam parent class Pertama
    def setTeam(self, team):
        self.team = team
        
    def showTeam(self):
        print(self.team) 
        
#membuat parent class kedua
class Tipe_Hero:
    
    #membuat method function didalam parent class kedua
    def setTipe(self, tipe):
        self.tipe=tipe
        
    def showTipe(self):
        print(self.tipe) #mencetak nilai dari method function sebelumnya didalam function lain
        
#membuat class turunan/warisan(Inheritance) dimana class turunan ini  merujuk ke dalam dua class parent sekaligus
class Hero(Team,Tipe_Hero):
    
    #membuat constructor
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
#membuat object untuk mengisi nilai dari constructor didalam class inheritance
Ucup = Hero('Ucup',100)

#membuat object untuk memberikan nilai didalam class inheritance yang sudah merujuk ke class Team
Ucup.setTeam("Merah")

#membuat object untuk memberikan nilai didalam class inheritance yang sudah merujuk ke class Tipe_Hero
Ucup.setTipe("cundang")

#menampilkan nilai dari setiap function setter yang ada didalam masing"class parent dan sudah di inheritance/diwariskan
Ucup.showTeam()
Ucup.showTipe()
        