#membahas private Variable dan Protected variable

class Hero:
    
    #membuat class variable
    jumlah=0
    
    #membuat constructor
    def __init__(self,name,health):
        self.name=name
        self.health=health
        
        #membuat variable private/instance variable private ->private variable bisa digunakan hanya pada class itu sendiri ketika diwariskan maka ini tdk akan bisa berjalan
        #variable ini bisa digunakan ketika membuat method function didalam itu sendiri dengan hak akses public
        self.__private="private" #tanda private dan protected variable pada python diawali dengan underscore(_)
        
        #membuat protected variable->variable ini bisa diakses oleh class turunannya/extends
        self._protected="protected"
        
#membuat object untuk class Hero
lina=Hero("lina",100) #memberikan nilai pada parameter constructor class Hero

print(lina.__dict__) #untuk menampilkan attribute apa saja yang ada didalam class tersebut
print(lina._protected)
lina._protected="contoh variable protected"
print(lina.__dict__) #utuk menampilkan attribute apa saja yang ada didalam class Hero
print(lina._protected) #untuk menampilkan apakah nilai variabel protected berubah atau tidak