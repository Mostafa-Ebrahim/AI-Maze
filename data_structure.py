class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class Stack():
    def __init__(self):
        self.stack = []

    def add(self, node):
        self.stack.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.stack)

    def empty(self):
        return len(self.stack) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty stack")
        else:
            node = self.stack[-1]
            self.stack = self.stack[:-1]
            return node


class Queue(Stack):
    def remove(self):
        if self.empty():
            raise Exception("empty Queue")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node