




import random

class Wallet:
    def __init__(self, value):
        self.value = value



    
class Balloon:
    def __init__(self, color, worth, probability):
        self.color = color
        self.worth = worth
        self.probability = probability
    

    def inflate(self):
        random_value = random.randint(1, 100)
        if random_value <= (self.probability*100):
            self.worth += 5
        else:
            self.pop()


    def pop(self):
        self.worth = 0


