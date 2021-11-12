from tkinter import *

import tkinter.messagebox as tmsg
from tkinter import Toplevel
from pyqrcode import *

import base64
root = Tk()

root.title("Message Encryption and Decryption ")
root.geometry("1040x700+180+50")
root.maxsize(width=1040, height=601)
root.minsize(width=1040, height=601)


######################## def############################


def exit():
    yes = tmsg.askokcancel("Notification", "Are you sure you want to Quity..!")
    if yes == True:
        root.destroy()
    else:
        pass


Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


def clear():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))


#
title = Label(root, text="Encryption and Decryption", bd=10, relief=GROOVE, font=("time new roman", "30", " bold"), bg="yellow",
              fg="crimson",
              height=1, width=45).place(x=0, y=5)


f1 = LabelFrame(root, text=" Product Details", font=("time new roman ", "13", "bold"), fg="crimson", bg='#55BEF9',
                relief=GROOVE, bd=10)
f1.place(x=0, y=75, relwidth=1)

lblMsg = Label(f1, text="MESSAGE", bg="#55BEF9", fg="black", width=16,
               font=("time new roman ", "13", "bold"), height=1, anchor=W)
lblMsg.grid(row=2, column=1, sticky="w", pady=4, padx=6)


lblkey = Label(f1, text="KEY (Only Integer) ", bg="#55BEF9", fg="black", width=16,
               font=("time new roman ", "13", " bold"), height=2, anchor=W)
lblkey.grid(row=3, column=1, sticky="w", pady=4, padx=6)


lblmode = Label(f1, text="MODE(e for encrypt,\nd for decrypt) ", bg="#55BEF9", fg="black", width=16,
                font=("time new roman ", "13", " bold"), height=2, anchor=W)
lblmode.grid(row=4, column=1, sticky="w", pady=4, padx=6)


lblResult = Label(f1, text="The Result-", bg="#55BEF9", fg="black", width=16,
                  font=("time new roman ", "13", " bold"), height=2, anchor=W)
lblResult.grid(row=5, column=1, sticky="w", pady=4, padx=6)


txtMsg = Entry(f1, width=22, font=(
    "time new roman ", "13", "bold"), bd=4, textvariable=Msg, insertwidth=4)
txtMsg.grid(row=2, column=2, sticky="w", pady=4, padx=6)

txtkey = Entry(
    f1, width=22, font=("time new roman ", "13", "bold"), bd=4, textvariable=key, insertwidth=4)
txtkey.grid(row=3, column=2, sticky="w", pady=4, padx=6)

txtmode = Entry(
    f1, width=22, font=("time new roman ", "13", "bold"), bd=4, textvariable=mode, insertwidth=4)
txtmode.grid(
    row=4, column=2, sticky="w", pady=4, padx=6)

txtResult = Entry(
    f1, width=22, font=("time new roman ", "13", "bold"), bd=4, textvariable=Result, insertwidth=4)
txtResult.grid(row=5, column=2, sticky="w", pady=4, padx=6)

info = "CORE TASK 3 (Encryption and Decryption) \nName: - Shaikh vasim Farukdin \nEmploye ID: - TEN/PD/1304 \nPosition:- (Python Developer – Associate)"
lblResult = Label(f1, text=info, bg="#55BEF9", fg="black", width=40,
                  font=("time new roman ", "13", " bold"), height=11, justify=LEFT)
lblResult.grid(row=6, column=4, sticky="w", pady=2, padx=2)


f2 = Frame(root, bg='yellow', relief=GROOVE, bd=10)
f2.place(x=0, y=520, width=1550, height=71)


Show = Button(f2, text="Show Message", command=Results, width=12, font=("time new roman ", "14", "bold"),
              relief=GROOVE, bd=5,
              bg="crimson", fg="white").place(x=230, y=0)
clear_Qr_btn = Button(f2, text="Clear", width=12, command=clear, font=("time new roman ", "14", "bold"), relief=GROOVE,
                      bd=5,
                      bg="crimson", fg="white").place(x=430, y=0)
exit_Qr_btn = Button(f2, text="Exit", width=12, command=exit, font=("time new roman ", "14", "bold"), relief=GROOVE,
                     bd=5, bg="crimson", fg="white").place(x=630, y=0)


root.mainloop()
