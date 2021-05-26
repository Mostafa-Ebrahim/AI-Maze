ffrom data_structure import *
from publicFunctions import *

def dfs(self):
    startNode = Node(state=self.start, parent=None)
    availableNodes = []
    self.visitedNodes = set()
    availableNodes.append(startNode)
    while True:
        if len(availableNodes) == 0:
            print("No solution")
            break
        currentNode = availableNodes.pop(-1)
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
                print("Actions: "+', '.join(actions))
                return

        self.visitedNodes.add(currentNode.state)

        # Add available nodes
        for action, state in self.availableActions(currentNode.state):
                if state not in self.visitedNodes:
                    child = Node(state=state, parent=currentNode, action=action)
                    availableNodes.append(child)  
