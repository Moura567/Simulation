import random
class Client:
    inter_arrival_time = 0
    type = '-'
    arrival_time = 0
    service_time = 0
    service_start_time = 0
    WaitingTimerg = 0
    WaitingTimeex = 0
    completion_time = 0
    total_time = 0
    cashierex = 0
    cashierereg = 0

    def __init__(self):
        self.inter_arrival_time = 0
        self.type = '-'
        self.arrival_time = 0
        self.service_time = 0
        self.service_start_time = 0
        self.WaitingTimeex = 0
        self.WaitingTimerg = 0
        self.completion_time = 0
        self.total_time = 0
        self.avpcashierex = 0
        self.avpcashierereg = 0

    def print(self):
        print("Inter arrival Time = ", self.inter_arrival_time)
        print("Customer type =", self.type)
        print("Arrival Time = ", self.arrival_time)
        print("Service Time = ", self.service_time)
        print("Service Start Time = ", self.service_start_time)
        print("Waiting Time EX = ", self.WaitingTimeex)
        print("Waiting Time RG = ", self.WaitingTimerg)
        print("Completion Time = ", self.completion_time)
        print("Total Time = ", self.total_time)
        print("Available Cashier EX = ", self.cashierex)
        print("Available Cashier EX = ", self.cashierereg)
        print("======================")
        return

    def generateType(self):
        a = Client.rand(self)
        x = '-'
        if 0 <= a < .6:
            x = 'E'
        elif .6 <= a <= 1:
            x = 'R'
        return x

    def generateIAT(self):
        b = Client.rand(self)
        if 0 <= b < .16:
            x = 0
        elif .16 <= b < .39:
            x = 1
        elif .39 <= b < .69:
            x = 2
        elif .69 <= b < .9:
            x = 3
        elif .9 <= b <= 1:
            x = 4
        return x

    def rand(self):
        r = round(random.uniform(0, 1), 2)
        return r

    def generateSt(a):
        c = Client.rand(a)
        if 0 <= c < .3 and a == 'E':
            x = 1
        elif .3 <= c < .70 and a == 'E':
            x = 2
        elif .70 <= c <= 1 and a == 'E':
            x = 3
        '''--------------------------------'''
        if 0 <= c < .2 and a == 'R':
            x = 3
        elif .2 <= c < .7 and a == 'R':
            x = 5
        elif .7 <= c <= 1 and a == 'R':
            x = 7
        return x

    def lenOfQueue(self,x, arr):
        z = 0
        t = 0
        i = 1
        for i in range(x):
            if (arr[i] == arr[i - 1] and arr[i] > 0):
                t += 1
            else:
                z = max(z, t)
                t = 0
            z = max(z, t)
        return z

    def MaxOfQueue(self,x, arr):
        z = 0
        t = 0
        for i in range(x):
            if (arr[i] > 0):
                t += 1
            else:
                z = max(z, t)
                t = 0
            z = max(z, t)
        return z

    def numofwait(self,x, arr):
        z = 0
        t = 0
        for i in range(x):
            if (arr[i] > 0):
                t += 1
        return t
