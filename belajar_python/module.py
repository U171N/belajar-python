# cara ke.4 mengimport module(dengan memanggil semua data yang ada)
from module2 import *
# cara ketiga mengimport module(dengan memanggil beberapa data saja)
from module2 import tambah as t
# cara ketiga mengimport module(dengan memanggil beberapa data saja)
from module2 import tambah, kurang
# cara import module ke satu
import module2

# instansiasi object dan memberikan nilai argument terhadap function yang ada didalam module yang kita panggil
module2.tambah(5, 3)

# cara import module ke.2
# import module2 as math

# # instansiasi object terhadap function dan memberikan nilai argument dengan menggunakan file lain
# math.tambah(3, 4)

# math.kurang(5, 3)


# cara ketiga mengimport module(dengan memanggil beberapa data saja)

tambah(3, 4)
kurang(3, 5)
t(3, 5)

# cara ke.4 mengimport module(dengan memanggil semua data yang ada)
tambah(8, 9)
kurang(7, 3)
