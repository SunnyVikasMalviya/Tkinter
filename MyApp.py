from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("MyApp")
        self.pack(fill=BOTH, expand=1)

        tab = Menu(self.master)
        self.master.config(menu=tab)

        file = Menu(tab)
        show = Menu(tab)
        _help = Menu(tab)
        
        file.add_command(label="Save", command=self.printsomething)
        file.add_command(label="Exit", command=self.leave)
        
        show.add_command(label="Show Image", command=self.showImg)
        show.add_command(label="Show Text", command=self.showTxt)

        _help.add_command(label="?", command=self.printsomething)
        
        tab.add_cascade(label="File", menu=file)
        tab.add_cascade(label="Edit", menu=show)
        tab.add_cascade(label="Help", menu=_help)
          
        TMAButton = Button(self, text="Take Massive Action", command=self.leave)
        TMAButton.place(x=40, y=40)

    def printsomething(self):
        print("Button was pressed.")

    def showImg(self):
        load = Image.open("6571772.jpg")
        render = ImageTk.PhotoImage(load)
        
        img = Label(self, image=render)
        img.image = render
        img.place(x=70, y=70)
        #img.pack()

    def showTxt(self):
        text = Label(self, text="I am taking massive actions!")
        text.place(x=30, y=30)
        text.pack()
    
    def leave(self):
        exit()
        
root = Tk()
root.geometry("1400x696")
app = Window(root)
root.mainloop()
