from Game import game
from Balloon_classes import Wallet, Balloon
from Strategy1 import strategy1
from matplotlib import pyplot as plt
from Strategy2 import strategy2
from Strategy3 import strategy3




#Strategy 1

"""
y = [game(100, strategy1)[0] for i in range(100)]
x = list(range(len(y)))

plt.plot(x, y)
plt.show()

print(sum(y)/len(y))
"""


#Strategy 2
"""
y = [game(100, strategy2)[0] for i in range(100)]
x = list(range(len(y)))
plt.plot(x, y)
plt.show()

print(sum(y)/len(y))

"""



#Strategy 3
"""
y = [game(100, strategy3)[0] for i in range(20)]
x = list(range(len(y)))

plt.plot(x, y)
plt.show()

print(sum(y)/len(y))
"""


"""
averages = []

for i in range(10):
    y = [game(100, strategy3)[0] for i in range(20)]
    print(sum(y)/len(y))


#print(averages)


"""




#Strategy 4
"""
averages = []
for i in range(100):
    y = [game(100, strategy4)[0] for i in range(100)]
    x = list(range(len(y))) 
    averages.append(sum(y)/len(y))

y = averages
x = range(len(averages))
plt.plot(x, y)
plt.show()
"""
