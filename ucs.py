from data_structure import *
from publicFunctions import *

def ucs(self):
    self.num_visitedNodes = -2

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
        self.num_visitedNodes += 1

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
                print()
                print("Actions: "+', '.join(actions))
                print()
                print("Number of visited nodes: ", self.num_visitedNodes)
                return

        self.visitedNodes.add(currentNode.state)

        # Add available nodes
        for action, state in self.availableActions(currentNode.state):
                if state not in self.visitedNodes:
                    child = Node(state=state, parent=currentNode, action=action, heuristic=None, cost=cost(self, currentNode.state))
                    availableNodes.append(child)