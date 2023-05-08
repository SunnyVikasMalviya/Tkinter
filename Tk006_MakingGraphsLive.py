"""
Updates
- Additionally importing style and matplotlib animation.
- In Global constants, added a style to be used and a data file path for plotting graph.
- Created a new function animate that takes data from datafile and plots the graph. This takes interval in milliseconds as parameters to refresh the graph.
- In class PageThree, commented the plotting a graph snippet.
- At the end, added a call to animate function using matplotlib's animation library. 
- Created a samplePlottingData.txt file containing csv data of plotting. We can update this to see changes in the graph in the application.
"""
"""
Observations
- We can list all matplotlib styles using style.available.
- We need to pass full path to the data file even if when the file is in the same directory.
"""
import tkinter as tk            
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib import style
import matplotlib.animation as animation


#Global constant vars
LARGE_FONT = ("Verdana", 12)    
style.use("seaborn-v0_8-notebook")
dataFilePath = "O:\MVikLearnings\Tkinter\samplePlottingData.txt"

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(interval):
    pullData = open(dataFilePath, "r").read()
    dataList = pullData.split("\n")
    xList, yList = [], []
    for line in dataList:
        if len(line) > 1:
            x, y = map(int, line.split(","))
            xList.append(x)
            yList.append(y)
    a.clear()
    a.plot(xList, yList)


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
        #f = Figure(figsize=(5,5) , dpi=100)
        #a = f.add_subplot(111)
        #a.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 6, 2, 7, 9, 12, 23, 3, 33, 1])

        #Adding the graph canvas to frame
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #Adding the navigation toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


#Creating and object of SeaofBTCapp class: app
app = SeaofBTCapp()

#Adding animation to the graph frame
ani = animation.FuncAnimation(f, animate, interval=2000)

#Runs the application
app.mainloop()