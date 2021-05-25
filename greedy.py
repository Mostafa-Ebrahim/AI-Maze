from data_structure import *
from publicFunctions import *

def greedy(self):
    OverallCost  = 0
    goalNode = Node(state=self.goal, parent=None, action=None, direction='none', heuristic=0,cost=0)
    startNode = Node(state=self.start, parent=None, action=None, direction='Up', heuristic=0,cost=0)
    availableNodes = [] 
    visitedNodes = []

    availableNodes.append(startNode)
    while availableNodes > 0 :
        currentNode = availableNodes.pop(getMinH(availableNodes, startNode.heuristic))
        if currentNode.state in visitedNodes : continue
        visitedNodes.append(currentNode.state)

        if IsGoal(currentNode.state, goalNode):
            print('somecode') #Some Code 
            # Solution = {}
            # Solution['solution'] = currentNode['path']
            # Solution['expanededNodes'] = len(visitedNodes)
            # return Solution

        possibleActions = availableActions(self, startNode.state)
        # for action in possibleActions:
        #     nextState = getState(currentNode['state'], action)
        #     nextNode = {}
        #     nextNode['state'] = nextState
        #     nextNode['path'] = currentNode['path'][:]
        #     nextNode['path'].append(action)
        #     nextNode['H'] = Heuristic(nextState)
        #     fringe.append(nextNode)


def getMinH(fringe, key):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i][key] < fringe[Min][key]:
            Min = i
    Min

def IsGoal(currentState,goal):
    if currentState == goal.state :
        return True
    return False 