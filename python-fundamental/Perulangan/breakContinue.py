print(50*"=")
print(" PROGRAM BREAK DAN CONTINUE  ")
print(50*"=")

j = 1
while(j < 11):
    if j == 4:
        print("4 tidak diceteak karena semua baris dilewati")
        j = j+1
        continue

    if j > 8:
        print(j, " lebih besar dari 8,maka program selesai")
        break
    print(j)
    j = j+1
