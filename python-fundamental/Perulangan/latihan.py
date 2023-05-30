print("Latihan pertama penerapan looping")
print(50*"=")

i = 6
while i >= 1:
    for j in range(1, i, 1):
        print(j, " ", end=" ")
    print("")

    i = i-1
