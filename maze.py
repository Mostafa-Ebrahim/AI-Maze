import bfs
import dfs
import astar
import greedy
import ucs
from data_structure import *

class Maze():
    def __init__(self, filename):
        with open(filename) as file:
            contents = file.read()

        # Determine height and width of maze
        contents = contents.splitlines()    #Split a string into a list where each line is a list item
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Track the walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None


    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("░", end="")
                    # print(" ▣ ", end="")
                elif (i, j) == self.start:
                    print("S", end="")
                elif (i, j) == self.goal:
                    print("G", end="")
                elif solution is not None and (i, j) in solution:
                    print("•", end="")
                else:
                    print(" ", end="")
                    # print(" □ ", end="")
            print()
        print()

    def availableActions(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def bfs(self):
        self.bfs = bfs.bfs(self)

    def dfs(self):
        self.dfs = dfs.dfs(self)

    def astar(self):
        self.astar = astar.astar(self)

    def greedy(self):
        self.greedy = greedy.greedy(self)

    def ucs(self):
        self.ucs = ucs.ucs(self)