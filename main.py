import sys
from maze import *
import bfs
import dfs
import astar
import greedy
import ucs
from publicFunctions import *




def run():
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python main.py maze1.txt")
    maze = 'maze3.txt'
    m = Maze(maze)
    print("Maze: ")
    m.print()
    m.greedy()
    print()
    m.print()

run()