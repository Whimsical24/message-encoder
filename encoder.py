from tkinter import *
import random
import base64

root = Tk()
root.geometry("120*6000")

root.title("Message Encryption and Decryption")

Tops = Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,relief=SUNKEN)
f1.pack(side=LEFT)

#==========================

lblInfo = Label(Tops,font=('helvetica',50, 'bold'),
                 text="SECRET MESSAGING \N Vigenere Cipher",
                 fg="Black",bd=10,anchor='w')