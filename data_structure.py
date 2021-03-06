class Node():
    def __init__(self, state, parent, action, heuristic, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.cost = cost

class Stack():
    def __init__(self):
        self.fringe = []

    def add(self, node):
        self.fringe.append(node)

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