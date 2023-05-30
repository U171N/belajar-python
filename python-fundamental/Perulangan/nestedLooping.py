print(50*"=")
print("             PROGRAM NESTED LOOPING  ")
print(50*"=")

i = 1
while i <= 6:
    for j in range(1, i, 1):
        print(j, " ", end=" ")
    print("")
    i = i+1
