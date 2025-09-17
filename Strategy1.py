#Strategy 1:
#always pump once and cash out.



def strategy1(balloon, history=None):
    if balloon.worth == 5:
        return "yes"
    else:
        return "no"