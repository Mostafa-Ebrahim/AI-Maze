from data_structure import *

OverAllCost = 0

def heu(self, node):
    (r1, c1) = node
    (r2, c2) = self.goal
    return abs(r2 - r1) + abs (c2 - c1)

def getcost(self):
    global OverAllCost
    if self.direction == self.action:
        OverAllCost += 1
    else:
        OverAllCost += 2

def FinalCost():
    return(OverAllCost//2 + 2)