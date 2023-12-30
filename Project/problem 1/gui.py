import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import tkinter.messagebox

class gui:
    def display_table_in_gui(self,table,avgex,avgrg,avgwaitex,avgwaitrg,maxex,maxrg,probwait,ss,sss,trial):
        window = tk.Tk()
        window.title("Calendar")
        # Create a Text widget to display the table
        text_widget = tk.Text(window, height=200, width=240, fg='white')

        text_widget.pack()

        text_widget.configure(bg='black')

        # Get the table content
        table_content = table

        # Insert the table content into the Text widget
        statements = [
            "\n Average service time for Express =", str((sum(avgex) / trial)),
            "\n Average service time for Regular =", str((sum(avgrg) / trial)),
            "\n The average waiting time in the express cashier queue = ", str(sum(avgwaitex) / trial),
            "\n The average waiting time in the regular cashier queue =", str(sum(avgwaitrg) / trial),
            "\n The maximum express cashier queue length =", str(maxex),
            "\n The maximum regular cashier queue length =", str(maxrg),
            "\n The probability that a customer wait in the express cashier queue =",
            str((probwait / trial)), '%',
            "\n The portion of idle time of the express cashier =", str(ss / trial),
            "\n The portion of idle time of the regular cashier =", str(sss / trial)
        ]

        # Insert each statement into the Text widget
        for statement in statements:
            text_widget.insert(tk.END, statement)
        # Disable text widget for read-only
        text_widget.config(state=tk.DISABLED)

        # Run the Tkinter main loop
        window.mainloop()

    def graph(self,avgex,avgrg,avgwaitex,avgwaitrg):
        plt.hist(avgex)
        plt.ylabel('Number of iterators')
        plt.xlabel('Mean of service in express cashier')
        plt.title('Service in express cashier')
        plt.show()

        plt.hist(avgrg)
        plt.ylabel('Number of iterators')
        plt.xlabel('Mean of service in regular cashier')
        plt.title('Service in regular cashier')
        plt.show()

        plt.hist(avgwaitex)
        plt.ylabel('Number of iterators')
        plt.xlabel('Mean of waiting in express cashier')
        plt.title('Waiting in Express cashier')
        plt.show()

        plt.hist(avgwaitrg)
        plt.xlabel('Number of iterators')
        plt.ylabel('Mean of waiting in regular cashier')
        plt.title('Waiting in regular cashier')
        plt.show()
    
    def messege(self):
        top = Tk()  # creating the main window
        top.title('Simulation for queuing system')  # setting title of the window
        top.geometry('300x100')  # setting the size of the window


        def func():  # function of the button
            tkinter.messagebox.showinfo("Greetings", "HELLO! YOU SHOULD CLOSE THE TEXT BOX TO SEE THE RESULT OF SIMULATING.")


        btn = Button(top, text="Simulate", width=17, height=3, command=func, fg='black', bg='red')
        btn.place(x=90, y=17)
        top.mainloop()  # running the loop that works as a trigger

