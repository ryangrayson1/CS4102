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
# Your Computing ID:
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################

class Node():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

class StoreGroup():
    def __init__(self, id, idoffset, stores, links):
        self.id = id
        self.idoffset = idoffset
        self.stores = stores
        self.links = links

class PRDGroup():
    def __init__(self, prds, links):
        self.prds = prds
        self.links = links

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

    def parse_file_stores(self, file):
        #Step 1: create all store and distribution center groups
        nodes, total_links = file[0].split()
        nodes = int(nodes)
        total_links = int(total_links)
        ids = 0
        i = 1
        store_groups = []
        sg = 0
        while i <= nodes:
            name, node_type = file[i].split()
            if node_type[0] == 'd':
                stores = {}
                stores[name] = Node(ids, name, 'd')
                start_id = ids
                ids += 1
                
                j = i+1
                while j <= nodes:
                    n, t = file[j].split()
                    if t[0] != 's':
                        break
                    stores[n] = Node(ids, n, 's')
                    ids += 1
                    j += 1

                new_sg = StoreGroup(sg, start_id, stores, [])
                store_groups.append(new_sg)
                sg += 1
                i = j
            else:
                i += 1
        
        while i <= nodes + total_links:
            n1, n2, cost = file[i].split()
            for j in range(len(store_groups)):
                if n1 in store_groups[j].stores and n2 in store_groups[j].stores:
                    store_groups[j].links.append([n1, n2, cost])

            i += 1

        return store_groups

    def parse_file_prds(self, file):
        nodes, total_links = file[0].split()
        nodes = int(nodes)
        total_links = int(total_links)
        i = 1
        prds = {}
        ids = 0
        while i <= nodes:
            n, t = file[i].split()
            if t[0] != 's':
                prds[n] = Node(ids, n, t)
                ids += 1
            i += 1

        links = []
        while i <= nodes + total_links:
            n1, n2, cost = file[i].split()
            if n1 in prds and n2 in prds and (prds[n1].type != 'd' or prds[n2].type != 'd'):
                links.append([n1, n2, cost])
            i += 1

        newprd = PRDGroup(prds, links)
        return newprd


    #will do kruskals on a certain subset of nodes and links and return the total cost of the MST
    def kruskals(self, nodes, links, idoffset): 
        n = len(nodes)

        links = sorted(links, key=lambda x: x[2])

        disjointsets = DisjointSet(n)
        li = 0
        edges_in_tree = 0
        cost = 0
        while edges_in_tree < n - 1:
            sw = links[li] # smallest weight edge
            node1 = nodes[sw[0]]
            node2 = nodes[sw[1]]
            set1 = disjointsets.findSet(node1.id - idoffset)
            set2 = disjointsets.findSet(node2.id - idoffset)
            if set1 != set2:
                edges_in_tree += 1
                cost += int(sw[2])
                disjointsets.union(set1, set2)
            li += 1
        return cost

    def min_cost(self, file_data):
        cost = 0
        #Step 1: perform Kruskal's on each "store group"
        sgs = self.parse_file_stores(file_data)
        for sg in sgs:
            cost += self.kruskals(sg.stores, sg.links, sg.idoffset)

        #Step 2: perform Kruskal's on groups with ports, rail hubs, and dist centers
        all_prds = self.parse_file_prds(file_data)
        cost += self.kruskals(all_prds.prds, all_prds.links, 0)
        
        return cost