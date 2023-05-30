#contoh program cara mengubah nialai pada variable global
def editNilaiVar():
    global x 
    print('nilai variable global x sebelum diubah: ',x)
    x = "Hai"
    print('nilai variable global x setelah diubah: ',x)
    
x = "Test"
editNilaiVar()

print('nilai variable x diluar scope prosedur setelah diubah: ',x)
