from data_structure import *

def heu(self, node):
    (r1, c1) = node
    (r2, c2) = self.goal
    return abs(r2 - r1) + abs (c2 - c1)

def getMinH(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].heuristic < fringe[Min].heuristic:
            Min = i
    return Min

def FinalCost(actions):
    cost = 0
    for i in range(1, len(actions)):
        if actions[i] == actions[i-1] and actions[0] == "up":
            cost+=1
        else:
            cost+=2
    return cost