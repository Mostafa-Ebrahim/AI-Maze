from data_structure import *

def dfs(self):
 startNode = Node(
        state=self.start, parent=None, action=None, direction="up", path=[]
    )
    availableNodes = []
    visitedNodes = []
 availableNodes.append(startNode)
    while len(availableNodes) > 0:
        currentNode = availableNodes.pop(-1)
         if currentNode.state in visitedNodes:
            continue
        visitedNodes.append(currentNode.state)
         if currentNode.state == self.goal:
             return currentNode.path[], len(visitedNodes)
        possibleActions = availableActions(self, startNode.state)
         for action in possibleActions:
             nextState = avaiableState(self, startNode.state, startNode.action)
             nextNode = node(state=nextState, path=[startNode.path,action] )
             action.append(nextNode)
             availableNodes.append(nextNode.path)
    return 'not found'         
