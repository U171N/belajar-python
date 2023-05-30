x=0
y=0
pangkat=1

def masukan():
    global x,n
    x=input("masukan nilai x : ")
    n=input("masukan niali n : ")
    
def hitung():
    global x,n,pangkat
    for i in range(int(n)):
        pangkat=pangkat*int(x)
        
def tampil():
    print(x,"pangkat",n,"=",pangkat)

masukan()
hitung()
tampil()