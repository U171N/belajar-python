print('     LATIHAN MEMBUAT PROGRAM DENGAN PYTHON       ')
print(50*'=')
nama=input('Nama: ')
tanggal=input('Tanggal: ')
print(50*'=')
print(      '===MENU==='        )
print("1.Es Teh     Rp.3000")
print("2.Jahe Susu  Rp.10000")
print("3.Teh Tarik  Rp.6000")
print("4.MilkShake  Rp.12000")
print(      "===MENU===="       )
h=[]
a=1
menu_pesanan=int(input('Masukan menu pesanan(No menu) : '))
if menu_pesanan==1:
    harga = 3000

elif menu_pesanan==2:
    harga = 10000

elif menu_pesanan==3:
    harga = 6000

elif menu_pesanan==4:
    harga = 12000

else:
    while True:
        print("===Menu Tidak tersedia.Silahkan pilih menu lainnya===")
        menu_pesanan=int(input("Masukan menu pesanan(No menu) : "))
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4:
            if menu_pesanan == 1:
                harga =3000
            elif menu_pesanan == 2:
                harga = 10000

            elif menu_pesanan == 3:
                harga = 6000

            elif menu_pesanan == 4:
                harga = 12000
            break
        jumlah_pembelian = int(input('Masukan jumlah pembelian: '))
        for i in range(jumlah_pembelian):
            h.append(harga)
        while True:
            jawab = input('Apakah ada yang ingin ditambahkan/Dikurangi? tambah/kurang/tidak?')
            if jawab =='tambah':
                tambah.int(input("Masukan menu pesanan(No menu) : "))
                if tambah ==1:
                    harga = 3000
                elif tambah ==2:
                    harga = 10000
                elif tambah == 3:
                    harga = 6000
                elif tambah == 4:
                    harga = 12000
                jumlah_tambahan = int(input("Masukan Jumalh Pembelian : "))
                for i in range(jumlah_tambahan):
                    h.append(harga)
                c = jumlah_tambahan + jumlah_pembelian
                print("Total Pembelian: ",c)
                bayar = sum(h)
                print("Total pembayaran: Rp.{}".format(bayar))
                break
            elif jawab == 'kurang':
                kurang = int(input("Berapa Jumlah yang akan dikurangkan? : "))
                for x in range(kurang):
                    if kurang <=1:
                        a -= kurang
                        del h[a]
                        bayar = sum(h)
                    else:
                        kurang -=a
                        del h[kurang]
                        if kurang < 0:
                            break
                c= jumlah_pembelian - kurang
                print("Total Pembelian: ",c)
                bayar = sum(h)
                print("Total pembayaran: Rp.{}",format(bayar))
                break
            else:
                bayar = sum(h)
                c = jumlah_pembelian
                print("Total pembayaran: Rp.{}",format(bayar))
                break