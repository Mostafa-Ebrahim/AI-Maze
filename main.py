import sys
from maze import *
import bfs
import dfs
import astar
import greedy
import ucs





def run():
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py maze1.txt")

    m = Maze(sys.argv[1])
    print("Maze: ")
    m.print()
    m.greedy()

run()