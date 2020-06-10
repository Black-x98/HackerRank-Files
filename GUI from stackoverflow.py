from Tkinter import *

root = Tk()
root.geometry("400x400+250+250")
root.title("Hex Converter")

heading = Label(root, text="Simple Hex to Decimal Converter", font=('arial 15 bold'), fg="steelblue").pack()

entr_hex_val = Label(root, text="Enter Hex Value to Convert", font=('arial 13 bold')).place(x=10, y=50)

my_num = IntVar()
ent_box = Entry(root, width=50, textvariable=my_num).place(x=10, y=90)

def converter():
    hexdec = my_num.get()
    dec = int(hexdec, 16)
    lab = Label(root, text=("decimal value = "+ str(dec)), font=('arial 25 bold'), fg="red").place(x=10, y=200)

conv = Button(root, text="Convert", width=12, height=2, bg="lightgreen", command=converter).place(x=10, y=130)

root.mainloop()
