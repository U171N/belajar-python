# Contoh penerapan function __main__ terhadap module yang dipanggil didalam file berbeda
# __main__ digunakan ketika kita bekerja dengan menggunakan modul-modul atau dengan kata lain kegunaan __main__ adalah memanggil modul-modul tsb

from Main import testModule  # memanggil folder yang berisi modul __main__
from sains import packages2
testModule.tambah(3, 4)
testModule.kurang(5, 3)
print(__name__)

# contoh implementasi kedua pemanggilan fungsi __main__


def main():
    print('penerapan fungsi __main__ ')


# fungsi ini memanggil nama file dari hasil __main__
print(f'__name__ pada packages2.py : {packages2.a}')
