# import package GUI
import tkinter

main_window = tkinter.Tk()

# membuat function untuk menambahkan event didalam button


def event_tekan():
    label2 = tkinter.Label(main_window, text="contoh event pada button")
    label2.pack()


label = tkinter.Label(
    main_window, text="contoh penggunaan package GUI \n latihan Python GUI")
tombol = tkinter.Button(main_window, text="enter", command=event_tekan)
label.pack()
tombol.pack()  # ini digunakan untuk memasukan component kedalam panel GUI yang sudah dibuat
main_window.mainloop()
