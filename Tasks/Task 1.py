import random
from matplotlib import pyplot as plt
LaborCost=[]
def randC1():
    x=random.uniform(0, 1)
    if  x<0.1:
        c1=44
    elif x>0.1 and x < 0.3:
        c1=44
    elif x>0.3 and x<.7:
        c1=45
    elif x>0.7 and x<0.9:
        c1=46
    else:
        c1=47
    LaborCost.append(c1)
    return c1
PartsCost=[]
def randC2():
    x=random.uniform(0,1)
    c2 = 80+x*(100-80)
    PartsCost.append(c2)
    return c2
Demand=[]
def randX():
    x = random.normalvariate(15000, 4500)
    Demand.append(x)
    return int(x)
maxProfit=0
profit=[]
counterOfLoss=0
loss=[]
x=0
maxloss=0
avgProfit=0
profits=0
for i in range (1000000):
    x=(249-randC1()-randC2())*randX()-1000000
    profit.append(x)
    profits+=x
    maxProfit = max(x, maxProfit)
    if x<0:
        counterOfLoss+=1
        loss.append(x)
    if len(loss)==0:
        maxnloss='No loss'
    else:
        maxloss=min(x,maxloss)
print('Probability of loss', (counterOfLoss/1000000)*100,'%','\n')

print('Max profit = ', maxProfit,'\n')

print('Max loss = ', maxloss,'\n')

avgProfit=sum(profit)/len(profit)

print('Average profit =' , avgProfit,'\n')


plt.hist(LaborCost, density = True, bins=30)
plt.ylabel('probability of c1')
plt.xlabel('Values of c1')
plt.show()

plt.hist(PartsCost, density = True, bins=30)
plt.ylabel('probability of c2')
plt.xlabel('c2')
plt.show()

plt.hist(Demand, density = True, bins=30)
plt.ylabel('probability of x')
plt.xlabel('x')
plt.show()

plt.hist(profit, density = True, bins=30)
plt.ylabel('probability of profit')
plt.xlabel('Profit')
plt.show()
