"""
Updates
- Additionally importing ttk from tkinter. TTK is sort of like CSS for tkinter.
- In class SeaofBTCapp, added icon and window title or app title.
- In class PageOne and PageTwo, changed tk.Button to ttk.Button. 
"""
"""
Observations
- Interestingly enough, tk.Buttton has a parameter font that I had set to LARGE_FONT in the last tutorial.
    But ttk.Button doesn't have the font parameter. Hence I couldn't update the buttons in the class StartPage.
- The icon file needs to be a 16x16 (pixels) file with .ico file extension. Any other format of image file is not supported.
- Also, I had to provide the full path of the icon file while it worked for
"""
import tkinter as tk            
from tkinter import ttk
#In python 2, tkinter is called Tkinter

#Global constant vars
LARGE_FONT = ("Verdana", 12)    

#Inherit class Tk from tk module to SeaofBTCApp class
class SeaofBTCapp(tk.Tk):       
    """
    SeaofBTCapp class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize method for class SeaofBTCapp.
        """
        #Initializing inherited class
        tk.Tk.__init__(self, *args, **kwargs)

        #Adding an icon and title to our app
        tk.Tk.iconbitmap(self, default="O:\MVikLearnings\Tkinter\Icon2.ico")
        tk.Tk.wm_title(self, "Sea of BTC Client")

        #Defining our container which will contain all our frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #This dictionary stores all the pages
        self.frames = {}

        #Looping to tuple of all pages and initialing self.frames
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """
        Method to bring the requested frame to the front i.e. raise the required frame.
        """
        frame = self.frames[cont]
        frame.tkraise()


#This will be the starting page
class StartPage(tk.Frame):          #Inheriting Frame class from tk module to StartPage class.
    """
    Class for Start Page.
    """

    def __init__(self, parent, controller):
        """
        Initialize method for class StartPage.
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="My first GUI App Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonPageOne = tk.Button(self, text="Go to Page 1", 
                                  command=lambda: controller.show_frame(PageOne), 
                                  font=LARGE_FONT)
        buttonPageOne.pack()
        buttonPageTwo = tk.Button(self, text="Go to Page 2", 
                                  command=lambda: controller.show_frame(PageTwo),
                                  font=LARGE_FONT)
        buttonPageTwo.pack()

class PageOne(tk.Frame):
    """
    Class for Page One.
    """

    def __init__(self, parent, controller):
        """
        Initialize method for class PageOne.
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="You just navigated to Page 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonStartPage = ttk.Button(self, text="Go to Start Page", 
                                    command=lambda: controller.show_frame(StartPage))
        buttonStartPage.pack()
        buttonPageTwo = ttk.Button(self, text="Go to Page 2", 
                                  command=lambda: controller.show_frame(PageTwo))
        buttonPageTwo.pack()

class PageTwo(tk.Frame):
    """
    Class for Page Two.
    """

    def __init__(self, parent, controller):
        """
        Initialize method for class Page Two.
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="You just navigated to Page 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonStartPage = ttk.Button(self, text="Go to Start Page", 
                                    command=lambda: controller.show_frame(StartPage))
        buttonStartPage.pack()
        buttonPageOne = tk.Button(self, text="Go to Page 1", 
                                  command=lambda: controller.show_frame(PageOne))
        buttonPageOne.pack()


#Creating and object of SeaofBTCapp class: app
app = SeaofBTCapp()

#Runs the application
app.mainloop()