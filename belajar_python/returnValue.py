# contoh penerapan return value dengan sebuah function
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah:', total)
    return total


# instansiasi objek dengan menambahkan sebuah argumen
a = kuadrat(4)  # mengasosiasikan variable total ke variable a
print(a)

print("")

# contoh penerapan return value dengan sebuah function dan multiple parameter


def tambah(argumen1, argumen2):
    ttl = argumen1+argumen2
    print(argumen1, '+', argumen2, '=', ttl)
    return ttl


n = tambah(5, 5)
print(n)

print("")

# contoh penerapan return value dengan sebuah callback function


def plus(args1, args2):
    total1 = args1+args2
    print(args1, '+', args2, '=', total1)
    return total1

# membuat function baru untuk callback function plus


def kali(opsi1, opsi2):
    total2 = opsi1*opsi2
    print(opsi1, 'X', opsi2, '=', total2)
    return total2


# instansia object dan menggabungkan argument pada callback function
b = kali(3, plus(3, 4))
print(b)
