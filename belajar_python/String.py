text = 'contoh string pada python'
print(text)

# penggunaan simbol backslish untuk menambahkan kutip
text2 = 'jalan-jalan pada hari jum\'at'
print(text2)

text3 = "jalan-jalan pada hari jum'at"
print(text3)

text4 = 'mahmud berkata, "kemarin kemana bro?"'
print(text4)

text5 = "alif menjawab,\"jalan-jalan bro\" "
print(text5)

# penggunaan \n untuk membuat baris baru
text6 = 'anisa: "kemarin kemana sis?"\nwidi:"main ke pantai"'
print(text6)

text7 = """
Maimun:"kemarin kemana bro?"
faiz:"jalan-jalan bro"
Maimun:"jalan-jalan kemana bro?"
Faiz:"ke pantai bro"
"""  # contoh penggunaan multiple line pada string
print(text7)

# contoh penggunaan raw string untuk memanggil direktori sistem
text8 = r'C:/filesystem'
print(text8)

print(5*"wk")  # menggunakan operator assignment nilai terhadap print untuk mencetak/menampilkan nilai sesuai assignment dilakukan

# urutannya index string spt ini(urutan sebelum hruf awal pada nilai string itu indexnya adalah 0,dan nilai selnajutnya setelah nilai string tsb dipanggil baru diurutkan dari 1):
# spasi dalam index string juga dihitung
# |m|e|m|a|n|g|g|i|l| |i|n|d|e|x| |s|t|r|i|n|g|
# | | | | | | | | | | | | | | | | | | | | | | |
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
contoh1 = "memanggil index string"
index = contoh1[0]  # memanggil index ke.0 ->huruf m
print(index)

index2 = contoh1[-4]
print(index2)

index3 = contoh1[0:9]
print(index3)
