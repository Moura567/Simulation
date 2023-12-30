from prettytable import PrettyTable
from Client import Client
from gui import*
gui.messege(gui)
intial = 0
size =500
trial=20
WaitingTimeEX = [intial] * size
WaitingTimeRG = [intial] * size
AvpForEX = [intial] * size
AvpForRg = [intial] * size
totalserviceex = 0
totalservicerg = 0
counterex = 0
counterrg = 0
totaavgex = 0
totalavgrg = 0
maxwaitex = 0
maxwaitrg = 0
compex = []
comprg = []
avgex = []
avgrg = []
ss = 0
sss = 0
customer = []
avgwaitex = []
avgwaitrg = []
avgiat = 0
maxex=0
maxrg=0
probwait=0
idleex=[]
idlerg=[]
totalidleex=0
totalidlerg=0
def simulation():
    for j in range(size):
        cust = Client()
        cust.type = Client.generateType(Client)
        cust.inter_arrival_time = Client.generateIAT(Client)
        cust.service_time = Client.generateSt(cust.type)
        customer.append(cust)


table = PrettyTable()
for i in range(trial):
    averagewaitex=0
    averagewaitrg=0
    customer.clear()
    table.clear()
    totalwaitex=0
    totalwaitrg=0
    counter1=0
    counter2=0
    totalserviceex = 0
    totalservicerg = 0
    table.field_names = ["Customer", "Customer Type", "IAT"
        , "Arrival Time"
        , "Service Time"
        , "TimeService Start"
        , "Waiting Time EX "
        , "Waiting Time RG "
        , "Time Service End"
        , "Time in System"
        , "Avb for ex"
        , "Avb rg"]
    idleexx = 0
    idlergg = 0
    lastcomp = 0
    totalidlerg=0
    totalidleex=0
    comprg=[]
    compex=[]
    simulation()
    idleex.clear()
    idlerg.clear()
    for i in range(size):
        avgiat += customer[i].inter_arrival_time
        if (customer[i].type == 'E'):
            counterex += 1
            totalserviceex += customer[i].service_time
        else:
            counterrg += 1
            totalservicerg += customer[i].service_time
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
                comprg.append(customer[i].completion_time)
                idlerg.append(customer[i].service_start_time)
                totalidlerg+=customer[i].service_start_time
            else:
                comprg.append(customer[i].completion_time)
                idlerg.append(customer[i].service_start_time)
                totalidlerg+=customer[i].service_start_time
                
        else:
            customer[i].arrival_time = customer[i - 1].arrival_time + customer[i].inter_arrival_time
            if customer[i].type == 'E' and Client.lenOfQueue(Client, i, WaitingTimeRG) * 1.5 >= Client.lenOfQueue(
                    Client, i, WaitingTimeEX):
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
                elif customer[i].arrival_time < AvpForEX[i - 1]:
                    customer[i].service_start_time = AvpForEX[i - 1]
                    WaitingTimeEX[i] = customer[i].service_start_time - customer[i].arrival_time
                    customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                    customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                    AvpForEX[i] = customer[i].completion_time
                    AvpForRg[i] = AvpForRg[i - 1]
                    compex.append(customer[i].completion_time)
                if (len(compex) <= 1):
                    idleex.append(customer[i].service_start_time)
                    totalidleex+=customer[i].service_start_time

                else:
                    idleex.append(customer[i].service_start_time - compex[counter1])
                    totalidleex+=customer[i].service_start_time - compex[counter1]
                    counter1 += 1

            elif customer[i].type == 'R' or (
                    customer[i].type == 'E' and Client.lenOfQueue(Client, i, WaitingTimeRG) * 1.5 < Client.lenOfQueue(
                Client, i, WaitingTimeEX)):
                if (customer[i].arrival_time < AvpForRg[i - 1]):
                    x = Client.lenOfQueue(Client, i, WaitingTimeRG)
                    y = Client.lenOfQueue(Client, i, WaitingTimeEX)
                    customer[i].service_start_time = AvpForRg[i - 1]
                    WaitingTimeRG[i] = customer[i].service_start_time - customer[i].arrival_time
                    WaitingTimeEX[i] = 0
                    customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                    customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                    AvpForEX[i] = AvpForEX[i - 1]
                    AvpForRg[i] = customer[i].completion_time
                    comprg.append(customer[i].completion_time)
                else:
                    customer[i].service_start_time = customer[i].arrival_time
                    WaitingTimeRG[i] = 0
                    WaitingTimeEX[i] = 0
                    customer[i].completion_time = customer[i].service_start_time + customer[i].service_time
                    customer[i].total_time = customer[i].completion_time - customer[i].arrival_time
                    AvpForEX[i] = AvpForEX[i - 1]
                    AvpForRg[i] = customer[i].completion_time
                    comprg.append(customer[i].completion_time)
                if (len(comprg) <= 1):
                    idlerg.append(customer[i].service_start_time)
                    totalidlerg+=customer[i].service_start_time
                    
                else:
                    idlerg.append(customer[i].service_start_time - comprg[counter2])
                    totalidleex+=customer[i].service_start_time - comprg[counter2]

                    counter2 += 1
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
    print("=============================================")
    idleexx+=sum(idleex)
    idlergg+=sum(idlerg)
    ss += idleexx
    sss += idlergg
    print(table)
    avgwaitex.append(sum(WaitingTimeEX) / size)
    avgwaitrg.append(sum(WaitingTimeRG) / size)
    averagewaitrg=sum(WaitingTimeRG) / size
    averagewaitex=sum(WaitingTimeEX) / size
    statements = [
        "\n Average service time for Express =", str((totalserviceex / size)),
        "\n Average service time for Regular =", str((totalservicerg / size)),
        "\n The average waiting time in the express cashier queue = ", str(averagewaitex),
        "\n The average waiting time in the regular cashier queue =", str(averagewaitrg),
        "\n The maximum express cashier queue length =", str((Client.MaxOfQueue(Client, size, WaitingTimeEX))),
        "\n The maximum regular cashier queue length =", str((Client.MaxOfQueue(Client, size, WaitingTimeRG))),
        "\n The probability that a customer wait in the express cashier queue =",
        str((Client.numofwait(Client, size, WaitingTimeEX) / size)), '%',
        "\n The portion of idle time of the express cashier =", str(idleexx),
        "\n The portion of idle time of the regular cashier =", str(idlergg)
    ]
    maxwaitex = max((Client.MaxOfQueue(Client, size, WaitingTimeEX), maxwaitex))
    maxwaitrg = max((maxwaitrg, Client.MaxOfQueue(Client, size, WaitingTimeRG)))
    # Insert each statement into the Text widget
    for statement in statements:
        print(statement)
    if (counterrg == 0):
        totaavgex += totalserviceex / size
        avgex.append(totalserviceex / size)
        avgrg.append(0)

    elif (counterex == 0):
        totalavgrg += totalservicerg / size
        avgrg.append(totalservicerg / counterrg)
        avgex.append(0)

    else:
        totaavgex += totalserviceex / size
        totalavgrg += totalservicerg / size
        avgrg.append(totalservicerg / size)
        avgex.append(totalserviceex / size)
        totalwaitrg+=sum(WaitingTimeRG)/size
    maxex=max(maxex,maxwaitex)
    maxrg = max(maxrg, maxwaitrg)
    probwait+=(Client.numofwait(Client, size, WaitingTimeEX) / size)
print(probwait)
# Display the table in the GUI
gui.display_table_in_gui(gui,table,avgex,avgrg,avgwaitex,avgwaitrg,maxex,maxrg,probwait,ss,sss,trial)
gui.graph(gui,avgex,avgrg,avgwaitex,avgwaitrg)