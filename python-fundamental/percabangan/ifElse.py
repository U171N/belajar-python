nama = input("Masukan nama =")
ipk = input("Masukan IPK(0-4) =")

if float(ipk) >= 3:
    ket = "berhak mendapatkan beasiswa"
else:
    ket = "tidak berhak mendapatkan beasiswa"

print("Saudara", nama, ",Anda dinyatakan", ket)
