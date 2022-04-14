#Ryan Grayson
# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: rtg5xkh
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################

class Node():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

class DisjointSet():
    def __init__(self, n): #this is makeset
        self.sets = []
        for i in range(n):
            self.sets.append(i)

    def findSet(self, i):
        while 1:
            if i == self.sets[i]:
                return i
            i = self.sets[i]

    def union(self, i, j):
        l1 = self.findSet(i)
        l2 = self.findSet(j)
        self.sets[l1] = l2

class Supply:
    def __init__(self):
        return

    store_to_dc = {}
    dc_to_store = {}
    graph_nodes = {}
    valid_links = []
    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        return self.min_cost(file_data)


    def kruskals(self): 
        n = len(self.graph_nodes)
        links = sorted(self.valid_links, key=lambda x: x[2])

        disjointsets = DisjointSet(n)
        li = 0
        edges_in_tree = 0
        cost = 0
        while edges_in_tree < n - 1 and li < len(links):
            sw = links[li] # smallest weight edge
            node1 = self.graph_nodes[sw[0]]
            node2 = self.graph_nodes[sw[1]]
            set1 = disjointsets.findSet(node1.id)
            set2 = disjointsets.findSet(node2.id)
            if set1 != set2:
                edges_in_tree += 1
                cost += int(sw[2])
                disjointsets.union(set1, set2)
            li += 1
        return cost


    def parse_file(self, file):
        nodes, total_links = file[0].split()
        nodes = int(nodes)
        total_links = int(total_links)
        ids = 0
        i = 1
        while i < nodes + 1:
            name, type = file[i].split()
            self.graph_nodes[name] = Node(ids, name, type)
            ids += 1
            if type == 'dist-center':
                self.dc_to_store[name] = []
                j = i + 1
                while j < nodes+1:
                    n, t = file[j].split()
                    if t != 'store':
                        break
                    self.graph_nodes[n] = Node(ids, n, t)
                    ids += 1
                    self.dc_to_store[name].append(n)
                    self.store_to_dc[n] = name
                    j += 1
                i = j
            else:
                i += 1

        i = nodes + 1
        while i < nodes + total_links + 1:
            n1, n2, cost = file[i].split()
            if n1 in self.graph_nodes and n2 in self.graph_nodes:
                if self.valid_connection(n1, n2):
                    self.valid_links.append([n1, n2, cost])
            i += 1

    def valid_connection(self, n1, n2):
        t1 = self.graph_nodes[n1].type
        t2 = self.graph_nodes[n2].type
        n1 = self.graph_nodes[n1].name
        n2 = self.graph_nodes[n2].name
        if t1 == 'dist-center' and t2 == 'store':
            if n2 not in self.dc_to_store[n1]:
                return False
        elif t1 == 'store' and t2 == 'dist-center':
            if n1 not in self.dc_to_store[n2]:
                return False
        elif t1 == 'port' and t2 == 'store':
            return False
        elif t1 == 'rail-hub' and t2 == 'store':
            return False
        elif t1 == 'dist-center' and t2 == 'dist-center':
            return False
        elif t1 == 'store' and t2 == 'port':
            return False
        elif t1 == 'store' and t2 == 'rail-hub':
            return False
        return True
            

    def min_cost(self, file_data):
        #Step 1: remove all invalid edges
        self.parse_file(file_data)

        #Step 2: perform Kruskal's on the graph with only valid edges
        return self.kruskals()