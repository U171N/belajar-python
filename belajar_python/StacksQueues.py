from collections import deque
data = [1, 2, 3, 4, 5, 6]
print("data awal: ", data)

# contoh penerapan proses stacking/Stacks pada python
data.append(7)
print("data masuk: ", 7)
print("data update: ", data)
data.append(8)
print("data masuk: ", 8)
print("data update: ", data)

out = data.pop()  # method pop digunakan untuk menghapus data yang terakhir ditambahkan
print("data yang keluar: ", out)
print("data akhir: ", data)
print(50*"+")

# contoh implementasi dari Queues


antrian = deque([1, 2, 3, 4, 5])
print("data awal: ", antrian)

# menambahkan data baru
antrian.append(6)
print("data masuk: ", 6)
print("data update: ", antrian)

antrian.append(7)
print("data masuk: ", 7)
print("data update: ", antrian)

# mengurangi antrian
keluar = antrian.popleft()
print("data keluar: ", keluar)
print("data sekarang: ", antrian)

# perbedaan stack dan Queues
# 1.jika menggunakan stack maka data yang terakhir ditambahkan akan dikeluarkan terlebih dahulu ketika menambahkan method pop
# 2.jika menggunakan Queues maka data yang sudah ada akan dikeluarkan terlebih dahulu sesuai urutannya
