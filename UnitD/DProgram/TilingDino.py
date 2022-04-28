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

import networkx

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
        BIPARTITE MATCHING - like a chess board
        '''
        pixels = 0
        G = networkx.DiGraph()
        G.add_node('source')
        G.add_node('target')
        #add all pixels as nodes
        for i in range(r):
            for j in range(c):
                if lines[i][j] == '#':
                    pixels += 1
                    if i % 2 == j % 2:
                        G.add_node('w ' + str(j) + ' ' + str(i))
                        G.add_edge('source', 'w ' + str(j) + ' ' + str(i), capacity=1)
                    else:
                        G.add_node('b ' + str(j) + ' ' + str(i))
                        G.add_edge('b ' + str(j) + ' ' + str(i), 'target', capacity=1)
        if pixels % 2 != 0:
            return ["impossible"]
        
        #find the valid edges, which represent a possible tile
        for i in range(r):
            for j in range(c):
                if lines[i][j] == '#':
                    if i % 2 == j % 2:
                        cur = 'w'
                    else:
                        cur = 'b'
                    if j+1 < c and lines[i][j+1] == '#':
                        if cur == 'w':
                            G.add_edge('w ' + str(j) + ' ' + str(i), 'b ' + str(j+1) + ' ' + str(i), capacity=1)
                        else:
                            G.add_edge('w ' + str(j+1) + ' ' + str(i), 'b ' + str(j) + ' ' + str(i), capacity=1)
                    
                    if i+1 < r and lines[i+1][j] == '#':
                        if cur == 'w':
                            G.add_edge('w ' + str(j) + ' ' + str(i), 'b ' + str(j) + ' ' + str(i+1), capacity=1)
                        else:
                            G.add_edge('w ' + str(j) + ' ' + str(i+1), 'b ' + str(j) + ' ' + str(i), capacity=1)
         
        mf = networkx.maximum_flow(G, 'source', 'target')
        mf = list(mf)
        tiles = []
        if mf[0] == pixels // 2:
            for e in mf[1]:
                if e[0] == 'w':
                    for k in mf[1][e]:
                        if mf[1][e][k] == 1:
                            c1, x1, y1 = e.split(' ')
                            c2, x2, y2 = k.split(' ')
                            tiles.append(x1 + ' ' + y1 + ' ' + x2 + ' ' + y2)

            return tiles

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