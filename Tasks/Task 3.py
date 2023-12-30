import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

intial = 0
size = 1000000
InterArrivalTime = [intial] * size
ArrivalTime = [intial] * size
ServiceStart = [intial] * size
ServiceTime = [intial] * size
WaitingTime = [intial] * size
Completion = [intial] * size
TimeInSystem = [intial] * size
AvailableForServer1 = [intial] * size
AvailableForServer2 = [intial] * size
minn = 0
maxx = 5
counter = 0
utz1=0
utz2=0
table = PrettyTable()
table.field_names = ["Customer","IAT", "AT", "SST", "WT", "ST", "CT", "Time in System", "Available Time for server 1", "Available Time for server 2"]


def generateIAT():
    # uniform distribution
    x = np.random.uniform(0, 1)
    r = minn + x * (maxx - minn)
    return r


def generateST():
    # normal distribution
    x = np.random.normal(2, .5)
    return x


x = round(0, 2)

for i in range(size):
    InterArrivalTime[i] = round(generateIAT(), 2)
    ServiceTime[i] = round(generateST(), 2)

for i in range(size):
    if (i == 0):
        ArrivalTime[i] = round(x + InterArrivalTime[i], 2)
        ServiceStart[i] = round(ArrivalTime[i], 2)
        Completion[i] = round(ServiceTime[i] + ServiceStart[i], 2)
        TimeInSystem[i] = round(Completion[i] - ArrivalTime[i], 2)
        AvailableForServer1[i] = Completion[i]
        AvailableForServer2[i] = 0.0
        utz1=ServiceTime[i]

    else:
        ArrivalTime[i] = InterArrivalTime[i] + ArrivalTime[i - 1]
        if (ArrivalTime[i] > AvailableForServer1[i - 1] or ArrivalTime[i] > AvailableForServer2[i - 1]):
            ServiceStart[i] = ArrivalTime[i]
        else:
            ServiceStart[i] = min(AvailableForServer1[i - 1], AvailableForServer2[i - 1])
        WaitingTime[i] = round(ServiceStart[i] - ArrivalTime[i], 2)
        if (WaitingTime[i] > 0):
            counter += 1
        Completion[i] = round(ServiceStart[i] + ServiceTime[i], 2)
        TimeInSystem[i] = round(Completion[i] - ArrivalTime[i], 2)
        if ((ArrivalTime[i] < AvailableForServer1[i - 1]) and ArrivalTime[i] > AvailableForServer2[i - 1]):
            AvailableForServer2[i] = Completion[i]
            AvailableForServer1[i] = AvailableForServer1[i - 1]
            utz2=utz2+ServiceTime[i]
        elif ((ArrivalTime[i] > AvailableForServer1[i - 1]) and ArrivalTime[i] < AvailableForServer2[i - 1]):
            AvailableForServer1[i] = Completion[i]
            AvailableForServer2[i] = AvailableForServer2[i - 1]
            utz1 = utz1 + ServiceTime[i]

        else:
            if (AvailableForServer1[i - 1] < AvailableForServer2[i - 1]):
                AvailableForServer1[i] = Completion[i]
                AvailableForServer2[i] = AvailableForServer2[i - 1]
                utz1 = utz1 + ServiceTime[i]
            else:
                AvailableForServer2[i] = Completion[i]
                AvailableForServer1[i] = AvailableForServer1[i - 1]
                utz2 = utz2 + ServiceTime[i]
        f=Completion[i]
for i in range(15):
    table.add_row([i+1,round(InterArrivalTime[i], 2)
                      , round(ArrivalTime[i], 2)
                      , round(ServiceStart[i], 2)
                      , round(WaitingTime[i], 2)
                      , round(ServiceTime[i], 2)
                      , round(Completion[i], 2)
                      , round(TimeInSystem[i], 2)
                      , round(AvailableForServer1[i], 2)
                      , round(AvailableForServer2[i], 2)])
print(table)
z=0
t=0
for i in range(size):
    if(WaitingTime[i]>0):
        t+=1
    z=max(z,t)

print("Average waiting time ", sum(WaitingTime) / size)
print("Number of customers had wait",counter)
print("utz time of simulation ",f)
print("Probability of waiting ", (counter / size) * 100)
print("Utilization for ATMS= ",sum(ServiceTime)/f)
print("Utilization for ATM1= ",round(utz1/max(AvailableForServer1),3))
print("Utilization for ATM2= ",round(utz2/max(AvailableForServer2),3))
print("Maximum number in queue ",z)
print("Average time in system ", sum(TimeInSystem) / size)

plt.hist(WaitingTime,  bins = 35)
plt.ylabel('Number of customers')
plt.xlabel('Waiting time')
plt.show()
