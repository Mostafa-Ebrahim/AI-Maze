from data_structure import *
from publicFunctions import *

def greedy(self):
    startNode = Node(state=self.start, parent=None, action=None, direction='Up', heuristic=0,cost=0)
    x = availableActions(self, startNode.state)
    print(x)

