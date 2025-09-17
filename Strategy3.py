
#Strategy 3:
#tests each color 5 times
#Then, takes average of how long it survived and uses this to estimate its probability

def strategy3(balloon, history):

    
    #has only the history of the previous balloons of that color
    filtered_history = history

    if len(filtered_history) <= 5 :
        #too few such balloons yet
        return "yes"
    else:
        values = [element[0] for element in filtered_history]
        average_value = sum(values)/len(values)

        if balloon.worth > average_value:
            return "no"
        else:
            return "yes"