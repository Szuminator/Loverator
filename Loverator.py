import time
from tkinter import *
from PIL import Image, ImageTk
import random, time

root = Tk()
root.call('wm', 'iconphoto', root._w, PhotoImage(file='heart.png'))
root.title("Loverator3000")
root.geometry('900x600+320+100')
root.config(background="#F51D96")


def take():
    nameGet = name1.get()
    nameGet2 = name2.get()
    sign = "%"
    if (len(nameGet2) and len(nameGet2) > 0):
        precent = random.randrange(0, 101)
        for i in range(0, precent):
            ix = str(i) + "%"
            labelPrecentText = Label(root, text=ix, background="#fc4f4f", font=('sanserif', 15))
            labelPrecentText.place(x=425, y=200)
            labelPrecentText.place(x=425, y=200)
    else:
        labelPrecentText = Label(root, text="0%", background="#fc4f4f", font=('sanserif', 15))
        labelPrecentText.place(x=425, y=200)


name1 = Entry(root)
name1.config(
    background="#F51D96",
    bd=3,
    font='sanserif',
    borderwidth=2,
)
name1.place(x=70, y=300)
name2 = Entry(root)
name2.config(
    background="#F51D96",
    bd=3,
    font='sanserif',
    borderwidth=2,
)
name2.place(x=600, y=300)

image = Image.open("send.png")
img = image.resize((100, 100))
my_img = ImageTk.PhotoImage(img)

send = Button(root, image=my_img, command=take)
send.config(
    borderwidth=0,
    background="#F51D96",
    activebackground="#F51D96"
)
send.place(x=400, y=400, width=100, height=100)

imageWoman = Image.open("woman.png")
imgWoman = imageWoman.resize((200, 200))
my_imgWoman = ImageTk.PhotoImage(imgWoman)

labelWoman = Label(root, image=my_imgWoman, width=200, height=200, background="#F51D96")
labelWoman.place(x=80, y=50)

imageMan = Image.open("man.png")
imgMan = imageMan.resize((200, 200))
my_imgMan = ImageTk.PhotoImage(imgMan)

labelMan = Label(root, image=my_imgMan, width=200, height=200, background="#F51D96")
labelMan.place(x=610, y=50)

imageHeart = Image.open("heart.png")
imgHeart = imageHeart.resize((150, 150))
my_imgHeart = ImageTk.PhotoImage(imgHeart)
labelHeart = Label(root, image=my_imgHeart, width=150, height=150, background="#F51D96")
labelHeart.place(x=375, y=150)

root.mainloop()
