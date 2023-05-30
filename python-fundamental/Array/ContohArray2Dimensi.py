#membuat variable yang berisi array 
nilai = [[60,55,75,80],[65,90,95],[85,88,82,93]]
print(nilai)

#cara menambahkan data baru pada array 2 dimensi
nilai.insert(3,[45,17,8])

for a in nilai:
    for b in a:
        print(b,end  = " ")
        print()


#cara update value didalam array2dimensi
nilai[3]=[72,73]
nilai[0][3]=90 #artinya akan mengubah nilai pada data array 1 pada urutan ke.3 yaitu 80
for a in nilai:
    for b in a:
        print(b,end  = " ")
        print()
