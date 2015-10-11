#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
import spotify
import sys


from Tkinter import *
from ttk import Frame, Button, Style


class Example(Frame):
  
    def __init__(self, parent, screen_size):
        Frame.__init__(self, parent)   
        self.screen_size = screen_size
        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()


    def initUI(self):
        # root = Tk()
        # text = Text(root)

        self.parent.title("Music In Motion")


        # img = ImageTk.PhotoImage(Image.open(""))
        # panel = tk.Label(root, image = img)
        # panel.pack(side = "bottom", fill = "both", expand = "yes")
        # # username = 'quinceftw'
        # # token = util.prompt_for_user_token(username)
        # # sp = spotipy.Spotify(auth=token)
        # # playlists = sp.user_playlists(username)

        

        Label(self.parent, text = "MORE MUSIC").pack()
        Label(self.parent, text = "Song: ").pack()
        Label(self.parent, text = "Artist(s): ").pack()
        Label(self.parent, text = "Album: ").pack()
        self.style = Style()
        self.style.theme_use("default")
        t = Text(self.parent, x=20)
        t.insert(INSERT, "SONG TITLES")
        self.pack(fill=BOTH, expand=1)
        # img = track
        # quitButton = Button(self, text="Quit", command=self.quit)
        # quitButton.place(x=50, y=50)

    def centerWindow(self):
      
        # w = 290
        # h = 150

        # sw = self.parent.winfo_screenwidth()
        # sh = self.parent.winfo_screenheight()
        
        # x = (sw - w)/2
        # y = (sh - h)/2
        self.parent.geometry(self.screen_size)

def main():
  
    root = Tk()
    screen_width = str(root.winfo_screenwidth()//2)
    screen_height = str(root.winfo_screenheight()//2)
    screen_size = screen_width + "x" + screen_height + "+300+300"
    root.geometry(screen_size)
    ex = Example(root, screen_size)
    root.mainloop()  


if __name__ == '__main__':
    main()  