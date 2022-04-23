from tkinter import *
from tkinter import *
from tkinter import messagebox
import json
import pyttsx3
from difflib import get_close_matches

engine = pyttsx3.init()  #creating instance of engine class

#############################################################################
#functionality part
def search():
    data = json.load(open('data.json'))
    word = enterwordEntry.get()

    word = word.lower()

    if word in data:
        meaning = data[word]

        textArea.config(state=NORMAL)
        textArea.delete(1.0, END)
        for item in meaning:
            textArea.insert(END, u'\u2022' + item + '\n\n')

        textArea.config(state=DISABLED)

    elif len(get_close_matches(word, data.keys())) > 0:

        close_match = get_close_matches(word, data.keys())[0]

        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')

        if res == True:

            meaning = data[close_match]
            textArea.delete(1.0, END)
            textArea.config(state=NORMAL)
            for item in meaning:
                textArea.insert(END, u'\u2022' + item + '\n\n')

            textArea.config(state=DISABLED)

        else:
            textArea.delete(1.0, END)
            messagebox.showinfo('Information', 'Please type a correct word')
            enterwordEntry.delete(0, END)

    else:
        messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
        enterwordEntry.delete(0, END)

def clear():
    textArea.config(state=NORMAL)
    enterwordEntry.delete(0, END)
    textArea.delete(1.0, END)
    textArea.config(state=DISABLED)

def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res == True:
        root.destroy()

    else:
        pass

def wordaudio():
    voices = engine.getProperty('voices')

    #speed of voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)

    #volume of voice
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1)

    #gender of voice
    engine.setProperty('voice', voices[1].id)
    engine.say(enterwordEntry.get())
    engine.runAndWait()


def meaningaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(textArea.get(1.0, END))
    engine.runAndWait()

#########################################################################################

root = Tk()
#title creating
root.title("Talking Dictionary by Imran")
#width and height of window
root.geometry("1089x650+100+30")
root.resizable(0, 0)
# bgImage = PhotoImage(file = r'C:\Users\Mohammad imran khan\OneDrive\Desktop\Python Intern\bg.png')
bgImage = PhotoImage(file = 'bg.png')

bgLabel = Label(root, image=bgImage)
# bgLabel.pack(side=TOP)
bgLabel.place(x=0,y=0)
# bgL abel.grid(row=0, column=0)

enetrwordlabel = Label(root, text="Enter word", font=("castellar", 27, "bold"), fg="red3", bg="whitesmoke")
enetrwordlabel.place(x=530, y=20)

enterwordEntry = Entry(root, font= ('arial', 23, 'bold'), justify='center', bd = 8, relief= GROOVE)
enterwordEntry.place(x=510,y=70)

searchImage = PhotoImage(file = 'search.png')
searchButton = Button(root, image=searchImage, bd=0, bg = 'whitesmoke', cursor='hand2', activebackground='whitesmoke'
                      ,command = search)
searchButton.place(x=600, y=150)

micImage = PhotoImage(file='mic.png')
micButton= Button(root, image=micImage, bd=0, bg = 'whitesmoke', cursor='hand2', activebackground='whitesmoke'
                  ,command=wordaudio)
micButton.place(x=700, y=153)

meaningwordlabel = Label(root, text="Meaning", font=("castellar", 27, "bold"), fg="red3", bg="whitesmoke")
meaningwordlabel.place(x=570, y=250)

textArea = Text(root, width=28, height= 6, font = ('arial', 18, 'bold'), bd = 8, relief=GROOVE)
textArea.place(x=510, y=300)

audioImage = PhotoImage(file='microphone.png')
audioButton= Button(root, image=audioImage, bd=0, bg= 'whitesmoke',cursor='hand2', activebackground='whitesmoke'
                    ,command=meaningaudio)
audioButton.place(x=530, y=530)

clearImage = PhotoImage(file='clear.png')
clearButton= Button(root, image=clearImage, bd=0, bg= 'whitesmoke',cursor='hand2', activebackground='whitesmoke'
                    , command=clear)
clearButton.place(x=650, y=530)

exitImage = PhotoImage(file='exit.png')
exitButton= Button(root, image=exitImage, bd=0, bg= 'whitesmoke',cursor='hand2', activebackground='whitesmoke'
                   ,command = iexit)
exitButton.place(x=770, y=530)

root.mainloop()