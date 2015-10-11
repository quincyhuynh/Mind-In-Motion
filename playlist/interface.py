#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
import spotify
import sys



from Tkinter import *
from ttk import Frame, Button, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()


    def initUI(self):
        # root = Tk()
        # text = Text(root)

        self.parent.title("Music In Motion")


        img = ImageTk.PhotoImage(Image.open(""))
        panel = tk.Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        # username = 'quinceftw'
        # token = util.prompt_for_user_token(username)
        # sp = spotipy.Spotify(auth=token)
        # playlists = sp.user_playlists(username)

        

        Label(self.parent, text = "MORE MUSIC").pack()
        Label(self.parent, text = "Song: ").pack()
        Label(self.parent, text = "Artist(s): ").pack()
        Label(self.parent, text = "Album: ").pack()
        self.style = Style()
        self.style.theme_use("default")
        t = Text(self.parent, x=10)
        t.insert(INSERT, "SONG TITLES")
        self.pack(fill=BOTH, expand=1)
        img = track
        # quitButton = Button(self, text="Quit", command=self.quit)
        # quitButton.place(x=50, y=50)

    def centerWindow(self):
      
        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    ex = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  