import sys
from maze import *
from publicFunctions import *




def run():
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python main.py maze1.txt")
    maze = 'maze5.txt'
    m = Maze(maze)
    print("Maze: ")
    m.print()
    m.greedy()
    print()
    m.print()

run()