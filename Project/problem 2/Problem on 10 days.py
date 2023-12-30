from dealer import dealer
from gui import *
#gui.messege(gui)
size = 10
initial = 0
begininv = [initial] * size
beginshow = [initial] * size
demand = [2, 3, 1, 2, 3, 3, 3, 2, 1, 1]
shortage = [initial] * size
endinv = [initial] * size
endshow = [initial] * size
order = [initial] * size
review = 3
leadtime = [initial] * size
table = PrettyTable()
profit = 0
holdCost = 0
orderCost = 0
totalProfit = []
totalinv = 0
totalshow = 0
daysShortage = 0
table.field_names = ["Days", "begin inv", "begin show"
    , "demand"
    , "end inv"
    , "end show"
    , "shortage"
    , "order"
    , "lead time"
    , "Review"
    , "Daily net profit"
    , "Total profit"]

cars = []


def simulation(j):
    car = dealer()
    car.demand = demand[j]
    cars.append(car)


a = 5
for i in range(size):
    simulation(i)
    netprofit = 0
    if (i == 0):
        cars[i].order = a
        cars[i].begininv = 3
        cars[i].beginshow = 4
        x = 2
        leadtime[i] = x
        dealer.calccar(dealer, cars, i, demand)
    else:
        x -= 1
        leadtime[i] = x
        if x > 0:
            cars[i].begininv = cars[i - 1].endinv
            cars[i].beginshow = cars[i - 1].endshow
            dealer.calccar(dealer, cars, i, demand)
        elif x == 0 or x < 0:
            cars[i].begininv = cars[i - 1].endinv
            cars[i].beginshow = cars[i - 1].endshow
            testshow = 5 - cars[i - 1].endshow
            testinv = 10 - cars[i - 1].endinv
            a -= testshow
            cars[i].beginshow += testshow
            if a < 0:
                cars[i].beginshow += a
                a = 0
            a -= testinv
            cars[i].begininv += testinv
            if a < 0:
                cars[i].begininv += a
                a = 0
            dealer.calccar(dealer, cars, i, demand)
            x = 0
            if (leadtime[i - 1] == 0 or leadtime[i - 1] == '-'):
                leadtime[i] = '-'
            else:
                leadtime[i] = 0
        if review == 0:
            cars[i].order = 15 - (cars[i - 1].endinv + cars[i - 1].endshow)
            a = cars[i].order
            review = 3
            x = dealer.generateleadtime(dealer)
            leadtime[i] = x
    review -= 1
    profit = 10000 * abs(demand[i] - shortage[i])
    holdCost = 1000 * (cars[i].endinv + cars[i].endshow)
    if (cars[i].order > 0):
        orderCost = 20000
    else:
        orderCost = 0
    netprofit = profit - (holdCost)
    totalProfit.append( netprofit)
    totalinv += cars[i].endinv
    totalshow += cars[i].endshow
    if (shortage[i] > 0):
        daysShortage += 1
    table.add_row([i + 1, cars[i].begininv, cars[i].beginshow,
                   demand[i], cars[i].endinv,
                   cars[i].endshow, cars[i].shortage,
                   cars[i].order, leadtime[i], review, netprofit, totalProfit[i]])

avgshow = totalshow / size
avginv = totalinv / size
avgprofit = sum(totalProfit)

# Display the table in the GUI
gui.display_table_in_guifor10(gui, table, avgshow, avginv, avgprofit, daysShortage)
