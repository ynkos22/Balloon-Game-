# Balloon-Game-
Balloon Game + Strategies:

Game Description:
A sequence of n balloons each of a color (yellow, green, red, or blue) is shown to the player. At each turn, the player can decide to inflate or cash out how much the balloon is currently worth. Initially, each balloon is worth 5 units, and each time one inflates a balloon it is worth 5 units more. If the balloon pops, it is worth 0 units. Balloons with the same color is assigned the same probability of popping at any time one inflates it. The goal is to estimate the probability of each color well enough to not pop most of the balloons, but also inflate them as much as possible. 

File descriptions:

Balloon_classes.py: Making objects balloons and wallet for later use

Game.py: This is the game itself (you can manually play it here or apply a strategy)

Strategy_testing.py: Here I have plotted the performance of 1 trivial strategy and one moving-average-type strategy

The remaining files are the aforementioned strategies.
