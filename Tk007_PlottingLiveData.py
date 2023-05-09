"""
Updates
- Additionally importing requests, datetime, numpy and pandas.
- In class PageOne, deleted button two.
- Deleted class PageTwo.
- Renamed class PageThree to BTCe_Page.
- In class StartPage, deleted snippet for button 2; updated buttons and their texts; added page warning message.
- In SeaofBTCapp class, updated all pages tuple.
- Indented driver code to main block.
- Updated the animate function.
"""
"""
Observations
- The graph is quiet ugly with lots of data in it. This needs to be fixed.
"""
import tkinter as tk            
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib import style
import matplotlib.animation as animation

import requests
from datetime import datetime

import numpy as np
import pandas as pd


#Global constant vars
LARGE_FONT = ("Verdana", 12)    
style.use("seaborn-v0_8-notebook")
#dataLink = "https://btc-e.com/api/3/trades/btc_usd?limit=2000"
dataLink = "https://cex.io/api/trade_history/BTC/USD/?status=200"    
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(interval):
    data = requests.request("GET", dataLink)
    data = data.json()
    df = pd.DataFrame(data)

    #Extracting buys data
    buys = df[(df["type"]=="buy")]
    buys["datestamp"] = [datetime.utcfromtimestamp(int(d)) for d in np.array(buys["date"])]
    buyDates = (buys["datestamp"]).tolist()
    
    #Extracting sells data
    sells = df[(df["type"]=="sell")]
    sells["datestamp"] = [datetime.utcfromtimestamp(int(d)) for d in np.array(sells["date"])]
    sellDates = (sells["datestamp"]).tolist()
    
    a.clear()
    a.plot_date(buyDates, buys["price"])
    a.plot_date(sellDates, sells["price"])


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
        for F in (StartPage, BTCe_Page):
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
        label = tk.Label(self, text=(
            """
            Warning!
            This application is in development and does not represent
             real world stocks. Users are advised to use it at their
            own discretion.
            """
        ), font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        buttonAgree = tk.Button(self, text="Agree",
                                    command=lambda: controller.show_frame(BTCe_Page),
                                    font=LARGE_FONT)
        buttonAgree.pack()
        buttonDisagree = tk.Button(self, text="Disagree", 
                                  command=quit,
                                  font=LARGE_FONT)
        buttonDisagree.pack()

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

class BTCe_Page(tk.Frame):
    """
    Class for BTCe_Page.
    This page contains the graph made using matplotlib.
    """

    def __init__(self, parent, controller):
        """
        Initialize method for BTCe_Page.
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonStartPage = ttk.Button(self, text="Back to Warning Page",
                                     command=lambda: controller.show_frame(StartPage))
        buttonStartPage.pack()

        #Adding the graph canvas to frame
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #Adding the navigation toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    #Creating and object of SeaofBTCapp class: app
    app = SeaofBTCapp()

    #Adding animation to the graph frame
    ani = animation.FuncAnimation(f, animate, interval=10000)

    #Runs the application
    app.mainloop()