import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
class gui:
    def messege(self):
        top = Tk()  # creating the main window
        top.title('Simulation for market system')  # setting title of the window
        top.geometry('300x100')  # setting the size of the window


        def func():  # function of the button
            tkinter.messagebox.showinfo("Greetings", "HELLO! YOU SHOULD CLOSE THE TEXT BOX TO SEE THE RESULT OF SIMULATING.")


        btn = Button(top, text="Simulate", width=17, height=3, command=func, fg='black', bg='red')
        btn.place(x=90, y=17)
        top.mainloop()  # running the loop that works as a trigger'''

    def display_table_in_gui(self,avgshow,avginv,avgprofit,daysShortage,x,y,table):
        window = tk.Tk()
        window.title("Calendar")

        # Create a Text widget to display the table
        text_widget = tk.Text(window, height=200, width=240, fg='white')

        text_widget.pack()

        text_widget.configure(bg='black')

        # Get the table content
        table_content = table

        # Insert the table content into the Text widget
        text_widget.insert(tk.END, table_content)

        statements = [
            "\n The average ending units in showroom = ", str(avgshow),
            "\n The average ending units in the inventory =", str(avginv),
            "\n The number of days when a shortage condition occurs = ", str(daysShortage),
            "\n The average net profit for the car dealer =", str(avgprofit),
            "\n The theoretical average demand =", str(1.34),
            "\n the experimental average demand =", str(x),
            "\n So we can say that it approximates match",
            "\n The theoretical average lead time  =", str(1.85),
            "\n the experimental average lead time =", str(y),
            "\n So we can say that it approximates match",

        ]

        # Insert each statement into the Text widget
        for statement in statements:
            text_widget.insert(tk.END, statement)
        # Disable text widget for read-only
        text_widget.config(state=tk.DISABLED)

        # Run the Tkinter main loop
        window.mainloop()

    def display_table_in_guifor10(self,table,avgshow,avginv,avgprofit,daysShortage):
        window = tk.Tk()
        window.title("Calendar")

        # Create a Text widget to display the table
        text_widget = tk.Text(window, height=200, width=240, fg='white')

        text_widget.pack()

        text_widget.configure(bg='black')

        # Get the table content
        table_content = table

        # Insert the table content into the Text widget
        text_widget.insert(tk.END, table_content)

        statements = [
            "\n The average ending units in showroom = ", str(avgshow),
            "\n The average ending units in the inventory =", str(avginv),
            "\n The number of days when a shortage condition occurs = ", str(daysShortage),
            "\n The average net profit for the car dealer =", str(avgprofit),
            "\n The theoretical average demand =", str(1.34),

        ]

        # Insert each statement into the Text widget
        for statement in statements:
            text_widget.insert(tk.END, statement)
        # Disable text widget for read-only
        text_widget.config(state=tk.DISABLED)

        # Run the Tkinter main loop
        window.mainloop()

    def graph(self,shortage,lead,demand):
        plt.hist(shortage)
        plt.ylabel('Number of iterators')
        plt.xlabel('Mean of shortage')
        plt.title('shortage')
        plt.show()

        plt.hist(lead)
        plt.ylabel('Number of iterators')
        plt.xlabel('Mean of lead time')
        plt.title('lead time')
        plt.show()

        plt.hist(demand)
        plt.ylabel('Number of iterators')
        plt.xlabel('Mean of demand')
        plt.title('demand')
        plt.show()