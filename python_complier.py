import tkinter as tk
import screen_config
from tkinter import Label,Entry,Button,StringVar, BOTH, OptionMenu, messagebox, Frame, Canvas, Scrollbar, RIGHT, ttk

class Python_Complier(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
    
    def start(self):
        X,Y = screen_config.srceen_config(self)
        for widget in self.winfo_children():
            widget.destroy()
        
        self.title('Python Complier') # This makes the window title 'login'
        self.configure(background='#AFF0F2')############

        # frame_main = Frame(self, bg='#ffffff')

        # canvas = Canvas(frame_main, bd=0, bg='#ffffff',  width=94*X, height=50*Y)
        # canvas.place(x=0,y=0)

        # frame = Frame(canvas, bg='#ffffff')

        # canvas.create_window(0, 0, anchor='nw', window=frame)
        # canvas.update_idletasks()




        # self.attributes("-fullscreen", True)
        self.mainloop()
    


    
    