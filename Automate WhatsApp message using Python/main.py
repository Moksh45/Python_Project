import pywhatkit
from PIL import ImageTk, Image
from tkinter import *
root = Tk()
root.title("Whatsapp Bot")
img = PhotoImage(file = '.\\whatsapp (1).png')
Label(root,image=img).pack()
Label(root, text="Enter No Where want to send message With country Code").pack()
number = Entry(root)
number.pack()
Label(root, text="Enter Your Message which You want to send ").pack()
message = Entry(root)
message.pack()
Label(root, text="Enter time in Hour").pack()
time_in_hour = Entry(root)
time_in_hour.pack()
Label(root, text="Enter Time in minute").pack()
min_of_time = Entry(root)
min_of_time.pack()


def send():
    pywhatkit.sendwhatmsg(number.get(), message.get(), int(time_in_hour.get()), int(min_of_time.get()))

Button(root, text="Send", command=send).pack()
root.bell()


root.mainloop()

