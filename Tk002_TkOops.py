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

        #
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
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
    Start Page class.
    """

    def __init__(self, parent, controller):
        """
        Initialize method for class StartPage.
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="My first GUI App Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


#Creating and object of SeaofBTCapp class: app
app = SeaofBTCapp()

#Runs the application
app.mainloop()