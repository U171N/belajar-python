# 15 nilai binernya yaitu=0000 1111 ->diubah menjadi 00111100(latihan operasi bitwise right shift)
a = 15
b = 13  # 13 nilai binernya yaitu=0000 1101
c = 0

print("Nilai a =", a, "atau 0000 1111")
print("Nilai b =", b, "atau 0000 1101")
print("")

# operator bitwise and(&)
c = a & b
print("operasi C=a&b menghasilkan nilai", c)
print("")
# operasi bitwise or(|)
c = a | b
print("operasis C=a|b menghasilkan nilai", c)
print("")
# operator bitwise XOR(^)
c = a ^ b
# hasilnya selisih nilai variable a dengan nilai variable b
print("operasi C=a^b menghasilkan nilai=", c)
print("")
# operator bitwise NOT(~)
c = ~a
print("operasi c=~a menghasilkan nilai=", c)
print("")
# operator bitwise right shift(operasi geser bit ke kanan) atau >>
c = a << 2
print("operasi c=a <<2 menghasilkan nilai", c)
print("")
# operasi bitwise left shift(operasi geser bit ke kiri) atau <<
c = a >> 2
print("operasi c = a>>2 menghasilkan Nilai", c)
