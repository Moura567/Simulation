import random


class dealer:
    begininv = 0
    beginshow = 0
    demand = 0
    shortage = 0
    endinv = 0
    endshow = 0
    order = 0
    review = 0

    def __init__(self):
        self.begininv = 0
        self.beginshow = 0
        self.demand = 0
        self.shortage = 0
        self.endinv = 0
        self.endshow = 0
        self.order = 0
        self.review = 0

    def geratedemand(self):
        x = random.uniform(0, 1)
        if 0 < x <= .2:
            return 0
        elif .2 < x <= 0.54:
            return 1
        elif 0.54 < x <= .9:
            return 2
        elif .9 < x <= 1:
            return 3

    def calccar(self, arr, i, demand):
        x = demand[i]
        if demand[i] <= arr[i].begininv:
            arr[i].endinv = arr[i].begininv - demand[i]
            arr[i].endshow = arr[i].beginshow
            arr[i].shortage = 0
        else:
            arr[i].endinv = 0
            x -= arr[i].begininv
            if x <= arr[i].beginshow:
                arr[i].endshow = arr[i].beginshow - x
                arr[i].shortage = 0
            else:
                arr[i].endshow = 0
                arr[i].shortage = x - arr[i].beginshow

    def generateleadtime(self):
        x = random.uniform(0, 1)
        if 0 < x <= 0.4:
            return 1
        elif 0.4 < x <= .75:
            return 2
        elif 0.75 < x <= 1:
            return 3

