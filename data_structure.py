class Node():
    def __init__(self, state, parent, action, direction, heuristic, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.direction = direction
        self.heuristic = heuristic
        self.cost = cost

    def setDirection(self, action):
        self.direction = action
class Stack():
    def __init__(self):
        self.fringe = []

    def add(self, node):
        self.fringe.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.fringe)

    def empty(self):
        return len(self.fringe) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty stack")
        else:
            node = self.fringe[-1]
            self.fringe = self.fringe[:-1]
            return node


class Queue(Stack):
    def remove(self):
        if self.empty():
            raise Exception("empty queue")
        else:
            node = self.fringe[0]
            self.fringe = self.fringe[1:]
            return node