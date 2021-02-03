from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Match Game!")
root.geometry("980x700")

matches = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]

random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict = {}


def button_click(b, number):
    global count, answer_list, answer_dict

    if b["text"] == ' ' and count < 2:
        b["text"] = matches[number]
        answer_list.append(number)
        answer_dict[b] = matches[number]
        count += 1

    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text="Match!!!")          
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_dict = {}
            answer_list = []
        else:
            my_label.config(text="DOH!")
            count = 0
            answer_list=[]
            messagebox.showinfo("Falsch!", "Falsch")
            for key in answer_dict:
                key["text"] = " "

            answer_dict = {}



b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b0, 0))
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b1, 1))
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b2, 2))
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b3, 3))
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b4, 4))
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b5, 5))
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b6, 6))
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b7, 7))
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b8, 8))
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b9, 9))
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b10, 10))
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b11, 11))
b12 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b12, 12))
b13 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b13, 13))
b14 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b14, 14))
b15 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b15, 15))
b16 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b16, 16))
b17 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b17, 17))
b18 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b18, 18))
b19 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b19, 19))
b20 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b20, 20))
b21 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b21, 21))
b22 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b22, 22))
b23 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b23, 23))
b24 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b24, 24))
b25 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b25, 25))
b26 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b26, 26))
b27 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b27, 27))
b28 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b28, 28))
b29 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=9, command=lambda: button_click(b29, 29))







b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)
b4.grid(row=0, column=4)
b5.grid(row=0, column=5)

b6.grid(row=1, column=0)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)
b10.grid(row=1, column=4)
b11.grid(row=1, column=5)

b12.grid(row=2, column=0)
b13.grid(row=2, column=1)
b14.grid(row=2, column=2)
b15.grid(row=2, column=3)
b16.grid(row=2, column=4)
b17.grid(row=2, column=5)

b18.grid(row=3, column=0)
b19.grid(row=3, column=1)
b20.grid(row=3, column=2)
b21.grid(row=3, column=3)
b22.grid(row=3, column=4)
b23.grid(row=3, column=5)

b24.grid(row=4, column=0)
b25.grid(row=4, column=1)
b26.grid(row=4, column=2)
b27.grid(row=4, column=3)
b28.grid(row=4, column=4)
b29.grid(row=4, column=5)


my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
