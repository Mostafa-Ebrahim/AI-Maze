from data_structure import *

OverAllCost = 0

def heu(self, node):
    (r1, c1) = node
    (r2, c2) = self.goal
    return abs(r2 - r1) + abs (c2 - c1)

def applyAction(self, currentNode, action):
    global OverAllCost
    if currentNode.direction == action[0]:
        OverAllCost += 1
    else:
        OverAllCost += 2
    newHeu = heu(self, currentNode)
    nextNode = Node(
        state=action[1],
        parent=currentNode,
        direction=action[0],
        heuristic=newHeu,
        cost=0,
        action=None,
    )
    return nextNode

def FinalCost():
    print(OverAllCost)