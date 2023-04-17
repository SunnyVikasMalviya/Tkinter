"""
Updates
- In class SeaofBTCapp, updated the initialization of self.frames by adding a for loop on a tuple of all pages.
- In class StartPage, added 2 buttons that navigate to different pages.
- Created new class PageOne and PageTwo similar to StartPage. These are the pages that we will navigate among.
"""

import tkinter as tk            
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

        buttonStartPage = tk.Button(self, text="Go to Start Page", 
                                    command=lambda: controller.show_frame(StartPage))
        buttonStartPage.pack()
        buttonPageTwo = tk.Button(self, text="Go to Page 2", 
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

        buttonStartPage = tk.Button(self, text="Go to Start Page", 
                                    command=lambda: controller.show_frame(StartPage))
        buttonStartPage.pack()
        buttonPageOne = tk.Button(self, text="Go to Page 1", 
                                  command=lambda: controller.show_frame(PageOne))
        buttonPageOne.pack()


#Creating and object of SeaofBTCapp class: app
app = SeaofBTCapp()

#Runs the application
app.mainloop()