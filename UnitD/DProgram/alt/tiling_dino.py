### Ryan Grayson
# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: rtg5xkh
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################

import networkx as nx

class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling 
    def compute(self, lines):
        self.print_image(lines)

        r = len(lines)
        c = len(lines[0])
        '''
        construct a graph such that each node is a possible connection between 2 black squares (a tiling)
        there is a directed edge between 2 of these "connection" nodes if:
            (1) they do not make use of the same node and 
            (2) the first node is above or to the left of the second node
        thus, the "top left" node is s and the "bottom right" node is t in the flow graph
        '''
        pixels = 0
        G = nx.DiGraph()
        first = []
        start_options = []
        for i in range(r):
            for j in range(c):
                if lines[i][j] == '#':
                    if len(first) == 0:
                        first = [i, j]
                        if j+1 < c and lines[i][j+1] == '#':
                            start_options.append(str(j) + ' ' + str(i) + ' ' + str(j+1) + ' ' + str(i))
                        if i+1 < r and lines[i+1][j] == '#':
                            start_options.append(str(j) + ' ' + str(i) + ' ' + str(j) + ' ' + str(i+1))
                    pixels += 1
                    if j+1 < c and lines[i][j+1] == '#':
                        G.add_node(str(j) + ' ' + str(i) + ' ' + str(j+1) + ' ' + str(i))
                    if i+1 < r and lines[i+1][j] == '#':
                        G.add_node(str(j) + ' ' + str(i) + ' ' + str(j) + ' ' + str(i+1))
        if pixels % 2 != 0:
            return ["impossible"]
        nodes = list(G.nodes)
        print(nodes)

        for i in range(len(nodes)):
            for j in range(i, len(nodes)):
                if i != j:
                    G.add_edge(nodes[i], nodes[j], capacity=1)

        G.add_node('source')
        G.add_node('target')
        for node in nodes:
            if node != 'source' and node != 'target':
                G.add_edge('source', node, capacity=1)
                G.add_edge(node, 'target', capacity=1)
        
        mf = nx.maximum_flow(G, 'source', 'target')
        print(mf)
        
        return ["impossible"]

    def print_image(self, lines):
        for line in lines:
            for c in line:
                if c == '.':
                    print("\U00002B1C", end="")
                elif c == '#':
                    print("\U00002B1B", end="")
            print()
        return
