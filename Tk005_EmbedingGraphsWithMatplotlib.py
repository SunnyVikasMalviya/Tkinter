"""
Updates
- Additionally importing matplotlib and a few more classes from matplotlib. We also use the backend TkAgg.
- In class SeaofBTCapp, added PageThree in the tuple of all pages.
- Created a new class PageThree. This page contains the plotted graph with navigation.
- In class StartPage, added a button to navigate to page three.
"""
"""
Observations
- FigureCanvasTkAgg doesn't have a show() method anymore. We need to use draw().
- NavigationToolbar2TkAgg is now NavigationToolbar2Tk. So we need to use "as" to rename imported module.
"""
import tkinter as tk            
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg

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
        for F in (StartPage, PageOne, PageTwo, PageThree):
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
        buttonPageThree = tk.Button(self, text="Go to Page 3",
                                    command=lambda: controller.show_frame(PageThree),
                                    font=LARGE_FONT)
        buttonPageThree.pack()

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


class PageThree(tk.Frame):
    """
    Class for Page Three.
    This page contains the graph made using matplotlib.
    """

    def __init__(self, parent, controller):
        """
        Initialize method for Page Three.
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonStartPage = ttk.Button(self, text="Go to Start Page",
                                     command=lambda: controller.show_frame(StartPage))
        buttonStartPage.pack()

        #Plotting the graph
        f = Figure(figsize=(5,5) , dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 6, 2, 7, 9, 12, 23, 3, 33, 1])

        #Adding the graph canvas to frame
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #Adding the navigation toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=False)


#Creating and object of SeaofBTCapp class: app
app = SeaofBTCapp()

#Runs the application
app.mainloop()