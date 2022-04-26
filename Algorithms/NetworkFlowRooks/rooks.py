### Ryan Grayson
'''
Task: given a grid of squares where the black squares represent a chess-like board (but could be any shape),
compute the maximum number of rooks that can be placed on the board without any rooks being able to capture each other.
We can solve this with bipartite matching and the ford-fulkerson network flow algorithm.
'''
import networkx

class MaxRooks:
    def __init__(self): 
        return

    def compute(self, lines):
        self.print_image(lines)
        r = len(lines)
        c = len(lines[0])

        G = networkx.DiGraph()
        G.add_node('source')
        G.add_node('target')
        #add all rows and colums that have a rook
        for j in range(r):
            for i in range(c):
                if lines[j][i] == '#':
                    G.add_node('r ' + str(j))
                    G.add_edge('source', 'r ' + str(j), capacity=1)
                    break
        for i in range(c):
            for j in range(r):
                if lines[j][i] == "#":
                    G.add_node('c ' + str(i))
                    G.add_edge('c ' + str(i), 'target', capacity=1)
                    break

        #add connection between a row and a column if they intersect at a rook
        for j in range(r):
            for i in range(c):
                if lines[j][i] == '#':
                    G.add_edge('r ' + str(j), 'c ' + str(i), capacity=1)

        mf = networkx.maximum_flow(G, 'source', 'target')
        mf = list(mf)
        return mf[0]

    def print_image(self, lines):
        for line in lines:
            for c in line:
                if c == '.':
                    print("\U00002B1C", end="")
                elif c == '#':
                    print("\U00002B1B", end="")
            print()
        return
