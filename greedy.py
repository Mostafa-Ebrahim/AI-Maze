from data_structure import *
from publicFunctions import *

def greedy(self):
    h=heu(self, self.start)
    startNode = Node(state=self.start, parent=None, action=None, direction="up", heuristic=h, cost=0)

    availableNodes = []
    self.visitedNodes = set()

    availableNodes.append(startNode)

    while True:
        if len(availableNodes) == 0:
            break

        currentNode = availableNodes.pop(getMinH(availableNodes))
        # reached the goal ?
        if currentNode.state == self.goal:
                actions = []
                cells = []
                while currentNode.parent is not None:
                    actions.append(currentNode.action)
                    cells.append(currentNode.state)
                    currentNode = currentNode.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

        self.visitedNodes.add(currentNode.state)

        # Add available nodes
        for action, state in self.availableActions(currentNode.state):
                if state not in self.visitedNodes:
                    child = Node(state=state, parent=currentNode, action=action, direction=currentNode.direction, heuristic=heu(self, currentNode.state), cost=getcost(currentNode))
                    availableNodes.append(child)

"""
        possibleActions = availableActions(self, startNode.state)
        # print(possibleActions)
        for action in possibleActions:
            nextNode = applyAction(self, currentNode, action)
            availableNodes.append(nextNode)
            # print('at end of for',availableNodes)
        # print('after for', availableNodes)
"""

def getMinH(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].heuristic < fringe[Min].heuristic:
            Min = i
    return Min
