from data_structure import *
from publicFunctions import *

def greedy(self):
    # print(self.goal)
    startNode = Node(
        state=self.start, parent=None, action=None, direction="up", heuristic=0, cost=0
    )
    availableNodes = []
    self.visitedNodes = []

    # print(getMinH(availableNodes, startNode.heuristic))
    # possibleActions = availableActions(self, startNode.state)
    # print(possibleActions[0][1])

    availableNodes.append(startNode)

    while len(availableNodes) > 0:
        print(len(availableNodes))

        # print('While Start', availableNodes)
        currentNode = availableNodes.pop(getMinH(availableNodes))
        
        '''
        if currentNode.state in self.visitedNodes:
            continue
        '''

        # reach the goal
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

        self.visitedNodes.append(currentNode.state)

        for action, state in self.availableActions(currentNode.state):
                if state not in self.visitedNodes:
                    child = Node(state=state, parent=currentNode, action=action, direction='up', heuristic=0, cost=None)
                    availableNodes.append(child)
"""
        possibleActions = availableActions(self, startNode.state)
        # print(possibleActions)
        for action in possibleActions:
            nextNode = applyAction(self, currentNode, action)
            availableNodes.append(nextNode)
            # print('at end of for',availableNodes)
        # print('after for', availableNodes)
    return FinalCost()
"""

def getMinH(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].heuristic < fringe[Min].heuristic:
            Min = i
    return Min
