import random
from Balloon_classes import Balloon, Wallet 
from matplotlib import pyplot as plt
from Strategy1 import strategy1

def game(how_many_rounds, strategy=None):

    
    #assigning a random probability for each color balloon
    probability_red = random.randint(1, 100) / 100
    probability_blue = random.randint(1, 100) / 100 
    probability_green = random.randint(1, 100) / 100
    probability_yellow = random.randint(1, 100) / 100


    
    #starting with 0 dollars
    wallet = Wallet(0)

    color_history = {
        "Red": [],
        "Blue": [],
        "Green": [],
        "Yellow": []
    }
    #selecting a random balloon
    for i in range(how_many_rounds):
        selected_balloon_color = random.choice(["Red", "Blue", "Green", "Yellow"])
        if selected_balloon_color == "Red":
            selected_balloon = Balloon("Red", 5, probability_red)
        elif selected_balloon_color == "Blue":
            selected_balloon = Balloon("Blue", 5, probability_blue)
        elif selected_balloon_color == "Green":
            selected_balloon = Balloon("Green", 5, probability_green)
        elif selected_balloon_color == "Yellow":
            selected_balloon = Balloon("Yellow", 5, probability_yellow)

        if strategy == None:
        #manual game:
        
            print(f"Balloon color: {selected_balloon.color}")
            
            while selected_balloon.worth != 0:
                choice = input("Do you want to inflate the balloon? (yes/no): ").strip().lower()
                if choice == 'yes':
                    selected_balloon.inflate()
                    if selected_balloon.worth != 0:
                        print(f"The balloon is inflated! Current worth: {selected_balloon.worth}")
                        continue
                    else:
                        print("The balloon popped!")
                        break
                else:
                    print(f"You cashed out with a worth of: {selected_balloon.worth}")
                    wallet.value += selected_balloon.worth
                    break
        else:
            #game controlled by strategy
            #stack is used to store the most recent balloon that has not popped yet
            stack = [1]
            


            while selected_balloon.worth != 0:
                #hasn't popped
                choice = strategy(selected_balloon, color_history[selected_balloon.color])
                if choice == 'yes':
                    #we want to inflate the ballon
                    #before we do so, let's store how much it is worth now in case it pops
                    #we remove the value that is on top and add the newest balloon
                    stack.pop()
                    stack.append(selected_balloon.worth)

                    selected_balloon.inflate()

                    if selected_balloon.worth != 0:
                        #it didn't pop!
                        stack.pop()
                        stack.append(selected_balloon.worth)
                        continue
                    else:
                        #it popped, so we can add the value it was worth before to history
                        color_history[selected_balloon.color].append([stack[-1], "P"])
                        break
                else:
                    #we cashed out 
                    #we also save how much we cashed out
                    wallet.value += selected_balloon.worth
                    color_history[selected_balloon.color].append([stack[-1], "C"])
                    break
    
    if strategy == None:
        print(f"Total wallet value: {wallet.value}\n")
        print(f"Probabilities were - Red: {probability_red}, Blue: {probability_blue}, Green: {probability_green}, Yellow: {probability_yellow}")

        #the history is in the following format:
        #color_history = {
        #Note if it was popped, the worth is its last value before popping, and if it was cashed out then it is the amount it was worth when cashing out
    return wallet.value, color_history






