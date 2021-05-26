from data_structure import *
from publicFunctions import *

def ucs(self):
    c=cost(self, self.start)
    startNode = Node(state=self.start, parent=None, action=None, heuristic=None, cost=c)

    availableNodes = []
    self.visitedNodes = set()

    availableNodes.append(startNode)

    while True:
        if len(availableNodes) == 0:
            print("No solution")
            break

        currentNode = availableNodes.pop(getMinC(availableNodes))
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
                print ("The Final Cost: ", FinalCost(actions))
                print("Actions: "+', '.join(actions))
                return

        self.visitedNodes.add(currentNode.state)

        # Add available nodes
        for action, state in self.availableActions(currentNode.state):
                if state not in self.visitedNodes:
                    child = Node(state=state, parent=currentNode, action=action, heuristic=0, cost=cost(self, currentNode.state))
                    availableNodes.append(child)