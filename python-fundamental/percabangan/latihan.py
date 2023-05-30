judul = "DATA NILAI MAHASISWA"
sub_judul = "NILAI AKHIR DAN GRADE"
print(judul.center(50, " "))
print(70*"-")

nama = input("Nama = ")
Tugas = int(input("Tugas = "))
Uts = int(input("Uts = "))
Uas = int(input("Uas = "))
print(70*"-")
print(sub_judul.center(50, " "))
print(70*"-")
NA = float((25 % Tugas)+(35 % Uts)+(40 % Uas))
if(float(NA) >= 80.0):
    Grade = "A"
elif(float(NA) >= 70.0):
    Grade = "B"
elif(float(NA) >= 60.0):
    Grade = "C"
else:
    Grade = "Tidak terdaftar"

print("Nama = ", nama)
print("Nilai Akhir = ", NA)
print("Grade = ", Grade)
print(50*"-")
