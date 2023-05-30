def prosedur():
    sapa = "Hai" #ini contoh menambahkan variable lokal didalam prosedur
    print(sapa)
    print(response)

response = "Hallo"
prosedur()

"""
Jika nama variable lokal dan global sama,semua nilai pada variablenya masih bisa diakses dikarenakan variable global terletak diluar scope prosedur
"""