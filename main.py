import sys
from maze import *
from publicFunctions import *




def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python main.py maze1.txt greedy")
    input = sys.argv[2]
    m = Maze(sys.argv[1])
    print()
    
    if input == 'astar':
        m.astar()
    elif input == 'bfs':
        m.bfs()
    elif input == 'dfs':
        m.dfs()
    elif input == 'greedy':
        m.greedy()
    elif input == 'ucs':
        m.ucs()
    
    print()
    m.print()

main()