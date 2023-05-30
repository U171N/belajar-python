nilai=[]
stop1=False
stop2=False
i=0

while(not stop1):
    jumlah = int(input("berapa data nilai,array ke-{}".format(i)))
    a=0
    tampung=[]
    
    for a in range(jumlah):
        nilai_baru=int(input("hasil inputan ke{11}".format(2)))
        tampung.append(nilai_baru)
    nilai.insert(i,tampung)
    i+=1
    tanya=input("apakah mau mengisi data lainnya?(y/t):")
    if(tanya=='t'):
        stop1=True
        
#mencetak table agar terlihat lebih rapi
print=("=====")
print("Cetak hasil")

for x in nilai:
    for b in x:
        print(b,end= "")
        print()