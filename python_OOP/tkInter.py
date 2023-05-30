#mengenal package tkInter untuk menampilkan versi GUI menggunakan python

import tkinter #import package library terlebih dahulu

#membuat object untuk merujuk pada clas tkinter
main_window=tkinter.Tk() #setiap class pada OOP menggunakan awalan huruf besar/kapital

#memasukan property pada object main_window
label=tkinter.Label(main_window,text="test")
tombol=tkinter.Button(main_window,text="Submit")

#method/function positioning untuk memanmpilkan nilai property pada object class tkinter
label.pack()
tombol.pack()

#method untuk meanmpilkan data property pada object class tkinter versi GUI
main_window.mainloop()
