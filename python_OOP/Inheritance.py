#membuat superclass atau class Induk

class Hero:
    
    
    #membuat constructor dengan parameter didalamnya
    def __init__(self,name,health):
        self.name=name #self adalah variable dengan visibility/hak akses privat
        self.health=health

#membuat class cabang/class pewarisan
class Hero_intelligent(Hero): #Hero didalam kurun ini merujuk ke superclass atau  class Induk
    pass


class Hero_strength(Hero):
    pass #pass ini artinya menyamakan constructor yang ada diclass induk

lina = Hero('lina',100)
techies=Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(lina.name) #menampilkan nilai dari parameter yang ada disebuah constructor
print(techies.name)
print(axe.name)
        