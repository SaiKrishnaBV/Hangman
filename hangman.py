from Tkinter import *
from PIL import Image, ImageTk
import time
global count, success,finish, word, tried
tried = []
finish = 0
word = ['s','a','i','k','r','i','s','h','n','a']
'''
Enter a word(upto 10 letters) for which you wish to play the game.
Incase you wish to use a word more than 10 letters you need to make a couple of changes.
#1
Change the Window Geometry, such that it can display blank spaces for all the characters of your word
<Line number 28>
600x200 implies width = 600 and height = 200
#2
Change the position where the image is being displayed according to your needs
<Lune number 62>
'''

count = 0
success = 0
images = []
pos = []
size = 150,150
window = Tk()
window.title("hangman")
window.configure(background='lavender')
window.geometry('600x200')
xpos = 0


def play():
    global count, success, finish, word, tried
    if(count <=6 and success!= len(word)):
        char = inp.get()
        if char in tried:
            warn = Toplevel()
            warn.title('Warning!')
            warn.geometry('300x100')
            lbl = Label(warn,text = "You have already entered this letter", font=("Times New Roman",10))
            lbl.place(x=0,y=0)
        elif char in word:
            tried.append(char)
            letter_freq = word.count(char)
            for i in range(letter_freq):
                position = word.index(char)
                pos[position].configure(state = "normal")
                pos[position].insert(0,char)
                success += 1
                word[position] = 0
                pos[position].configure(state = "readonly")
            if(success == len(word)):
                finish = 1
        else:
            tried.append(char)
            load = Image.open(images[count])
            count += 1
            load.thumbnail(size, Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(window, image = render)
            img.image = render
            img.place(x=400,y=50)
    if count == 7 or finish == 1:
        window.destroy()
        out = Tk()
        out.geometry('150x75')
        if success == 7:
            lbl = Label(out,text = "You Win", font=("Times New Roman",20))
            lbl.place(x=0,y=0)
        else:
            lbl = Label(out,text = "You Loose", font=("Times New Roman",20))
            lbl.place(x=0,y=0)   


for i in range(1,8):
    savename = "hangman" + str(i) + ".png"
    images.append(savename)
    
lbl = Label(window, text = "HANGMAN", font=("Times New Roman Bold Italic",20), bg = "lavender")
lbl.place(x = 200, y = 10)

lbl = Label(window, text = "Enter a letter: ", font=("Times New Roman Bold ", 10),bg = "lavender")
lbl.place(x = 20, y = 100)

inp = Entry(window, width = 4)
inp.place(x = 120, y = 100)

Button(window,text='Enter', command=play).place(x=120, y = 130)

for i in range(len(word)):
    e = Entry(window, width = 3, state = "readonly")
    e.place(x = xpos + 30, y = 60)
    xpos +=30
    pos.append(e)
window.mainloop()
