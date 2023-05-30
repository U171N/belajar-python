#cara menampilkan data dengan menggunakan looping
def VarLength(*Mhs):
    j=0
    for i in Mhs:
        j=j+1
        print("Nama ke-",j,"= ",i)
    return

VarLength("Fay","Mayza","Abdul","Sh")