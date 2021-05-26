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

def getMinH(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].heuristic < fringe[Min].heuristic:
            Min = i
    return Min

def FinalCost():
    return(OverAllCost//2 + 2)