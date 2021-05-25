from data_structure import *
from publicFunctions import *

OverAllCost = 0


def greedy(self):
    # print(self.goal)
    startNode = Node(
        state=self.start, parent=None, action=None, direction="up", heuristic=0, cost=0
    )
    availableNodes = []
    visitedNodes = []

    # print(getMinH(availableNodes, startNode.heuristic))
    # possibleActions = availableActions(self, startNode.state)
    # print(possibleActions[0][1])

    availableNodes.append(startNode)
    while len(availableNodes) > 0:
        # print('While Start', availableNodes)
        currentNode = availableNodes.pop(getMinH(availableNodes, heu))
        if currentNode.state in visitedNodes:
            continue
        visitedNodes.append(currentNode.state)

        # print ('after poping', availableNodes)
        if currentNode.state == self.goal:
            print("somecode")  # Some Code
            # Solution = {}
            # Solution['solution'] = currentNode['path']
            # Solution['expanededNodes'] = len(visitedNodes)
            # return Solution

        possibleActions = availableActions(self, startNode.state)
        # print(possibleActions)
        for action in possibleActions:
            nextNode = applyAction(self, currentNode, action)
            availableNodes.append(nextNode)
            # print('at end of for',availableNodes)
        # print('after for', availableNodes)
    return FinalCost()


def getMinH(fringe, heuristic):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].heuristic < fringe[Min].heuristic:
            Min = i
    return Min
