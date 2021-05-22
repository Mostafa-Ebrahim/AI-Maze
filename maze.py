import sys

class Maze():
    def __init__(self, filename):
        # Read file and set height and width of maze
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
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("•", end="")
                else:
                    print(" ", end="")
            print()
        print()

############################################################################################

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze: ")
m.print()
