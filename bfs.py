from data_structure import *
from publicFunctions import *

def bfs(self):
    self.num_visitedNodes = -2
    startNode = Node(state=self.start, parent=None, action=None, heuristic=0, cost=0)
    
    availableNodes = Queue()
    self.visitedNodes = set()
    
    availableNodes.add(startNode)

    while True:
        if availableNodes.empty():
            print("No solution")
            break
    
        currentNode = availableNodes.remove()
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
                    child = Node(state=state, parent=currentNode, action=action, heuristic=0, cost=0)
                    availableNodes.add(child)  
