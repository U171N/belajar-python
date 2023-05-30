class A:
    def show(self):
        print("show function di class A")
        
class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass #jika attribute yang ada diclass D Di pass/lewati,maka akan membaca data class lain yang ada didalam kurung sesuai urutannya(dari class B kemudian ke class C)

#menampilkan attribute yang ada di class D
object = D()
object.show()