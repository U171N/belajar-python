# package adalah kumpulan dari module-module yang berisi data dimana package ini akan diimport dalam sebuah file tersendiri
# cara import package dengan menggunakan __init__
import sains

# cara import salah satu module didalam package yang sudah dimasukan ke dalam __init__
# from sains import package3
speed = sains.kecepatan(100, 50)
print(speed)
# cara memanggil salah satu module didalam package yang sudah dimasukan didalam file init
# ini adalah salah satu function didalam module package yang dipanggil
test = sains.tambah(3, 4)
print(test)
