# Strategy4.py
import random
import numpy as np

# keep Beta priors for each color
priors = {
    "Red":  [1, 1],
    "Blue": [1, 1],
    "Green": [1, 1],
    "Yellow": [1, 1]
}

def update_priors(color, history):
    """Update priors based on the full history for this color."""
    alpha, beta = 1, 1  # reset priors
    for worth, outcome in history:
        if outcome == "P":   # balloon popped
            beta += 1
        elif outcome == "C": # balloon cashed successfully
            alpha += 1
    priors[color] = [alpha, beta]

def strategy4(balloon, history=None):
    """
    Thompson sampling: decide whether to inflate or cash out.
    """
    color = balloon.color
    
    # update priors from history
    update_priors(color, history)

    alpha, beta = priors[color]
    
    # sample survival probability from posterior
    sampled_theta = np.random.beta(alpha, beta)
    
    # expected value if inflating: probability of survival * (worth+5)
    expected_inflate = sampled_theta * (balloon.worth + 5)
    
    # expected value if cashing: guaranteed worth
    expected_cash = balloon.worth
    
    if expected_inflate > expected_cash:
        return "yes"
    else:
        return "no"
