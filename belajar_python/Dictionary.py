# Materi pengenalan tentang Dictionary
# syntax dasar dictionary: namaVariable={key:value}

# contoh implementasi dictionary
member1 = {"ID": 101,
           "Nama": "M Fakhruddin",
           "Status": "Mahasiswa"
           }
member2 = {"ID": 102,
           "Nama": "M Kurniawan",
           "Status": "Buruh"
           }
# ketika mencari data yang dipanggil adalah key bukan berdasarkan index
print(member1["ID"])
print("")
# contoh pemanggilan data berdasarkan key dictionary
print(member1.keys())
print("")
# contoh pemanggilan data berdasarkan values dictionary
print(member1.values())
print("")
# contoh pemanggilan semua data dictionary
print(member1.items())
print("")
# cara kedua dalam pemanggilan semua data yang ada didalam dictionary
print(member1)
print("")
# memanggil semua daftar dictionary
# memanggil dictionary berdasarkan value
memberlist = {101: member1, 102: member2}
print(memberlist[101])
print("")
print(memberlist[102])
