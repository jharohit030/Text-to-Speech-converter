from tkinter import *

from gtts import gTTS
import os  # this module helps to play the converted audio

root = Tk()
root.geometry("400x300")
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")

Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='Rohit', font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')

Msg = StringVar()
Label(root, text="Enter Text", font='arial 15 bold', bg='white smoke').place(x=20, y=60)
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


def Text_to_speech():
    language = "en"

    myobj = gTTS(text=entry_field.get(), lang=language, slow=False)
    myobj.save("Rohit.mp3")
    os.system("Rohit.mp3")


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


Button(root, text='PLAY', font='arial 15 bold', command=Text_to_speech, width='4').place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, width='4').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset, width='6').place(x=175, y=140)

root.mainloop()
