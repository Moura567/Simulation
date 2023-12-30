import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from Client import *

top = Tk()  # creating the main window
top.title('Simulation for queuing system')  # setting title of the window
top.geometry('300x100')  # setting the size of the window


def func():  # function of the button
    tkinter.messagebox.showinfo("Greetings", "HELLO! YOU SHOULD CLOSE THE TEXT BOX TO SEE THE RESULT OF SIMULATING.")


btn = Button(top, text="Simulate", width=17, height=3, command=func, fg='black', bg='red')
btn.place(x=90, y=17)
top.mainloop()  # running the loop that works as a trigger
intial = 0
size = 10
InterArrivalTime = [0,0,2,3,3,0,2,1,0,1]
ArrivalTime = [intial] * size
CustomerType = ['R', 'R', 'R', 'E', 'E','E', 'E','E', 'E','R']
SerivceTime = [5,5,3,3,1,1,1,2,1,5]
WaitingTimeEX = [intial] * size
WaitingTimeRG = [intial] * size
AvpForEX = [intial] * size
AvpForRg = [intial] * size
totalserviceex = 0
totalservicerg = 0
counterex = 0
counterrg = 0
idle = 0
table = PrettyTable()
lastcomp = 0
lastcompex=0
lastcomprg=0
compex = []
comprg = []
serviceex=[]
servicerg=[]
idleex=[]
idlerg=[]

customer = []
for i in range(size):
    cust = Client()
    cust.type = CustomerType[i]
    cust.inter_arrival_time = InterArrivalTime[i]
    cust.service_time = SerivceTime[i]
    customer.append(cust)

table = PrettyTable()
table.field_names = ["Customer", "Customer Type", "IAT"
    , "Arrival Time"
    , "Service Time"
    , "TimeService Start"
    , "Waiting Time EX "
    , "Waiting Time RG "
    , "Time Service End"
    , "Time in System"
    , "Avb for ex"
    , "Avb for rg"]
counter1=0
counter2=0
for i in range(size):
    if i == 0:
        customer[i].arrival_time = customer[i].inter_arrival_time
        customer[i].service_start_time = customer[i].arrival_time
        customer[i].WaitingTimeex = 0
        customer[i].WaitingTimerg = 0
        WaitingTimeEX[i] = 0
        WaitingTimeRG[i] = 0
        customer[i].completion_time = customer[i].service_time + customer[i].service_start_time
        customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
        AvpForRg[i] = customer[i].completion_time
        AvpForEX[i] = 0
        if (customer[i].type == 'E'):
            totalserviceex += customer[i].service_time
            counterex += 1
            #compex.append(customer[i].completion_time)
            idlerg.append(customer[i].service_start_time)
        else:
            totalservicerg += customer[i].service_time
            counterrg += 1
            comprg.append(customer[i].completion_time)
            idlerg.append(customer[i].service_start_time)
    else:
        customer[i].arrival_time = customer[i - 1].arrival_time + customer[i].inter_arrival_time
        if (customer[i].type == 'E'):
            totalserviceex += customer[i].service_time
            counterex += 1
        else:
            totalservicerg += customer[i].service_time
            counterrg += 1
        if customer[i].type == 'E' and Client.lenOfQueue(Client,i, WaitingTimeRG) * 1.5 >= Client.lenOfQueue(Client,i, WaitingTimeEX):
            if (customer[i].arrival_time >= AvpForEX[i - 1]):
                customer[i].service_start_time = customer[i].arrival_time
                WaitingTimeRG[i] = 0
                WaitingTimeEX[i] = 0
                customer[i].WaitingTimeex = 0
                customer[i].WaitingTimerg = 0
                customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                AvpForEX[i] = customer[i].completion_time
                AvpForRg[i] = AvpForRg[i - 1]
                compex.append(customer[i].completion_time)
                lastcompex=customer[i-1].completion_time
            elif customer[i].arrival_time < AvpForEX[i - 1]:
                customer[i].service_start_time = AvpForEX[i - 1]
                WaitingTimeEX[i] = customer[i].service_start_time - customer[i].arrival_time
                customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                AvpForEX[i] = customer[i].completion_time
                AvpForRg[i] = AvpForRg[i - 1]
                compex.append(customer[i].completion_time)
                lastcompex=customer[i-1].completion_time
            if(len(compex)<=1):
                idleex.append(customer[i].service_start_time)
            else:
                idleex.append(customer[i].service_start_time-compex[counter1])
                counter1+=1


        elif customer[i].type == 'R' or (
                customer[i].type == 'E' and Client.lenOfQueue(Client,i, WaitingTimeRG) * 1.5 < Client.lenOfQueue(Client,i, WaitingTimeEX)):
            if (customer[i].arrival_time < AvpForRg[i - 1]):
                x = Client.lenOfQueue(Client,i, WaitingTimeRG)
                y = Client.lenOfQueue(Client,i, WaitingTimeEX)
                customer[i].service_start_time = AvpForRg[i - 1]
                WaitingTimeRG[i] = customer[i].service_start_time - customer[i].arrival_time
                WaitingTimeEX[i] = 0
                customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                AvpForEX[i] = AvpForEX[i - 1]
                AvpForRg[i] = customer[i].completion_time
                comprg.append(customer[i].completion_time)
                lastcomprg=customer[i-1].completion_time
            else:
                customer[i].service_start_time = customer[i].arrival_time
                WaitingTimeRG[i] = 0
                WaitingTimeEX[i] = 0
                customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                AvpForEX[i] = AvpForEX[i - 1]
                AvpForRg[i] = customer[i].completion_time
                comprg.append(customer[i].completion_time)
                lastcomprg=customer[i-1].completion_time
            if (len(comprg) <= 1):
                idlerg.append(customer[i].service_start_time)
            else:
                idlerg.append(customer[i].service_start_time - comprg[counter2])
                counter2 += 1
    lastcomp = customer[i].completion_time

    if(customer[i].type=='R'):
        servicerg.append(customer[i].service_time)
    else:
        serviceex.append(customer[i].service_time)

    table.add_row([i + 1, customer[i].type, customer[i].inter_arrival_time
                      , customer[i].arrival_time
                      , customer[i].service_time
                      , customer[i].service_start_time
                      , WaitingTimeEX[i]
                      , WaitingTimeRG[i]
                      , customer[i].completion_time
                      , customer[i].total_time
                      , AvpForEX[i]
                      , AvpForRg[i]])

def display_table_in_gui():
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
        "\n Average service time for Express =", str(totalserviceex / size),
        "\n Average service time for Regular =", str(totalservicerg / size),
        "\n The average waiting time in the express cashier queue = ", str(sum(WaitingTimeEX) / size),
        "\n The average waiting time in the regular cashier queue =", str(sum(WaitingTimeRG) / size),
        "\n The maximum express cashier queue length =", str(Client.MaxOfQueue(Client,size, WaitingTimeEX)),
        "\n The maximum regular cashier queue length =", str(Client.MaxOfQueue(Client,size, WaitingTimeRG)),
        "\n The probability that a customer wait in the express cashier queue =",
        str((Client.numofwait(Client,size, WaitingTimeEX) / size)), '%',
        "\n The idle time of epress cashier =", str((sum(idleex))),
        "\n The idle time of regular cashier =", str((sum(idlerg))),

    ]

    # Insert each statement into the Text widget
    for statement in statements:
        text_widget.insert(tk.END, statement)
    # Disable text widget for read-only
    text_widget.config(state=tk.DISABLED)

    # Run the Tkinter main loop
    window.mainloop()
# Display the table in the GUI
display_table_in_gui()
plt.hist(serviceex)
plt.title('Service in express cashier')
plt.show()

plt.hist(servicerg)
plt.title('Service in regular cashier')
plt.show()

plt.hist(WaitingTimeEX)
plt.title('Waiting in Express')
plt.show()

plt.hist(WaitingTimeRG)
plt.xlabel('Number of iterators')
plt.ylabel('Mean of waiting in regular cashier')
plt.title('Waiting in Bank')
plt.show()