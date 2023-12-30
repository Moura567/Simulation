import random
orederd = 0
profits = []
def generatedemand():
    r = random.uniform(0, 1)
    if r >= 0 and r < 0.2:
        demand = 0
    elif r >= 0.2 and r < .6:
        demand = 1
    elif r >= 0.6 and r < .8:
        demand = 2
    elif r >= 0.8 and r < .9:
        demand = 3
    elif r >= 0.9 and r < 1:
        demand = 4
    return demand

s = 0
h = 0
for i in range(2):
    orederd += 1
    stored = 0
    demand = 0
    sold = 0
    unsold = 0
    penalty_storage = 0
    penalty_unsold = 0
    weekProfit = []
    avilable_pc = 0
    for i in range(500):
        avilable_pc = avilable_pc + orederd
        demand = generatedemand()
        if (demand > avilable_pc):
            sold = avilable_pc
            avilable_pc = 0
            penalty_unsold = (demand - avilable_pc) * 100
        elif (demand < avilable_pc):
            sold = demand
            avilable_pc -= demand
            penalty_storage = (avilable_pc - demand) * 50
        else:
            sold = demand
            penalty_storage = 0
            penalty_unsold = 0
        x = sold * 450
        loss = penalty_unsold + penalty_storage
        profit = x - loss
        if (orederd == 1 and profit >= 0):
            s += profit
        elif (orederd == 2 and profit >= 0):
            h += profit
print("Average profit for ordering 1 laptop per week : ", s / 500)

print("Average profit for ordering 2 laptop per week : ", h / 500)
if s/500> h/500:
    print("YOU SHOULD ORDER 1 LAPTOP PER WEEK")
else:
    print("YOU SHOULD ORDER 2 LAPTOP PER WEEK")