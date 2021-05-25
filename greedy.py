from data_structure import *
from publicFunctions import *

OverallCost = 0


def greedy(self):
    # print(self.goal)
    startNode = Node(
        state=self.start, parent=None, action=None, direction="Up", heuristic=0, cost=0
    )
    availableNodes = []
    visitedNodes = []

    print(getMinH(availableNodes, startNode.heuristic))
    # possibleActions = availableActions(self, startNode.state)
    # print(possibleActions[0][1])

    availableNodes.append(startNode)
    while len(availableNodes) > 0:
        currentNode = availableNodes.pop(getMinH(availableNodes, startNode.heuristic))
        if currentNode.state in visitedNodes:
            continue
        visitedNodes.append(currentNode.state)

        if IsGoal(self, currentNode.state):
            print("somecode")  # Some Code
            # Solution = {}
            # Solution['solution'] = currentNode['path']
            # Solution['expanededNodes'] = len(visitedNodes)
            # return Solution

        possibleActions = availableActions(self, startNode.state)
        for action in possibleActions:
            nextNode = applyAction(self, currentNode, action)
            #     nextNode = {}
            #     nextNode['state'] = nextState
            #     nextNode['path'] = currentNode['path'][:]
            #     nextNode['path'].append(action)
            #     nextNode['H'] = Heuristic(nextState)
            availableNodes.append(nextNode)

    print(OverallCost)


def getMinH(fringe, key):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i][key] < fringe[Min][key]:
            Min = i
    return Min


def IsGoal(self, currentState):
    if currentState == self.goal:
        return True
    return False


def applyAction(self, currentNode, action):
    if currentNode.direction == action[0]:
        OverallCost = +1
    else:
        OverallCost = +2
    newHeu = heu(self, currentNode)
    nextNode = Node(
        state=action[1],
        parent=currentNode,
        direction=action[0],
        heuristic=newHeu,
        cost=0,
    )
    return nextNode
