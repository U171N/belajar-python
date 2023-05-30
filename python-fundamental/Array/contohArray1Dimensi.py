buah=[]
stop=False
i=0

while(not stop):
    buah_baru = input("inputkan nama buah yang ke-{}:".format(1))
    buah.append(buah_baru)
    
    #update nilai
    i+=1
    tanya = input("mau ditambah lagi datanya(Y/T):")
    if(tanya=="T"):
        stop=True
        
        #cetak semua data buah
        print("hasil input nama buah : ",buah)