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
        #add all black squares as nodes for potential rooks
        for i in range(r):
            for j in range(c):
                if lines[i][j] == '#':
                    G.add_node('r ' + str(j) + ' ' + str(i))
                    G.add_edge('source', 'w ' + str(j) + ' ' + str(i), capacity=1)
        
         
        mf = networkx.maximum_flow(G, 'source', 'target')
        mf = list(mf)
        print(mf)

        return

    def print_image(self, lines):
        for line in lines:
            for c in line:
                if c == '.':
                    print("\U00002B1C", end="")
                elif c == '#':
                    print("\U00002B1B", end="")
            print()
        return
