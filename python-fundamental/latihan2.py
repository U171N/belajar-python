print("=========================")
print("     LATIHAN PYTHON      ")
print("=========================")
print("Kode NamaProduk  Harga   ")
print("=========================")
print("01   Ventella    Rp200000")
print("02   Patrobas    Rp220000")
print("03   Brodo       Rp300000")
print("=========================")

banyak_jenis=int(input("BanyakJenis: "))
kode_barang=[]
banyak_pasang=[]
nama_sepatu=[]
harga=[]
jumlah=[]

i=0

while i<banyak_jenis:
    print("jenis ke -",1+i)
    kode_barang.append(input("KodeBarang [0S/AS/SS]: "))
    banyak_pasang.append(int(input("Banyak Pasang: ")))
    
    if kode_barang[i]=="OS" or kode_barang[i]=="os":
        harga.append("200000")
        jumlah.append(banyak_pasang[i]*int("120000"))
        
    elif kode_barang[i]=='AS' or kode_barang[i]=="as":
        harga.append("220000")
        jumlah.append(banyak_pasang[i]*int("220000"))
    
    elif kode_barang[i]=='SS' or kode_barang[i]=='ss':
        harga.append("300000")
        jumlah.append(banyak_pasang[i]*int('300000'))
        
    else:
        nama_sepatu.append('Tdk ditemikan')
        harga.append("0")
        jumlah.append(banyak_pasang[i]*int("0"))

i=i+1

print("==========================================")
print("            =Latihan PYTHON=              ")
print("==========================================")
print("No    Nama     Harga    banyak   Jumlah   ")
print("==========================================")

jumlah_bayar=0
p=0

while p<banyak_jenis:
    jumlah_bayar=jumlah_bayar+jumlah[p]
    print("%i   %s  %s  %i"%(p+1,nama_sepatu[p],harga[p],banyak_pasang[p],jumlah[p]))
    p=p+1
print("============================================================================")
pajak=jumlah_bayar*5/100
total_bayar=jumlah_bayar+pajak
print("jumlah bayar= Rp.",jumlah_bayar)
print("Total bayar =Rp.",total_bayar)
