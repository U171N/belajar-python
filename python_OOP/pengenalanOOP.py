class Hero:  #class
    pass #code yang harus ada ketika membuat sebuah class pada python OOP

hero1=Hero() #merupakan object yang mengcu pada class Hero

#menambahkan sebuah properti kepada object hero1

hero1.name="sniper"
hero1.healt=200

print(hero1) #untuk mengecek apakah hero1 merupakan object dari class Hero atau bkn
print(hero1.__dict__) #menampilkan semua properti yang ada didlam object hero1
print(hero1.name) #untuk menampilkan nilai dari salah satu properti yang ada didlam object hero1
