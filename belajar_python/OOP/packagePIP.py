from PIL import Image

gambar = Image.open("foto.png")
print("format file: " + gambar.format)  # menampilkan format file gambar
# menampikan ukuran gambar,untuk menampilkan ukuran harus di parse ke string
print("ukuran file: " + str(gambar.size))
print("mode file:" + gambar.mode)  # menampikan mode gambar(rgb atau cmyk)
