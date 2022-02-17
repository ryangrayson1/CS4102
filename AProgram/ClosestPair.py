# CS4102 Spring 2022 - Unit A Programming 
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
# Collaborators: ra9ha
# Sources: Introduction to Algorithms, Cormen
#################################

class ClosestPair:
    def __init__(self):
        return

    mins = []
    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1 
    def compute(self, file_data): 
        srtd = self.to_sorted_list(file_data)
        if len(srtd) == 0 or len(srtd) == 1:
            return -1
        self.closest2(srtd)
        return self.mins

    #accepts the list of strings and returns a list of coordinate lists: [x, y] sorted by x coordinate
    def to_sorted_list(self, data):
        points = []
        for line in data:
            x, y = line.split()
            x = float(x)
            y = float(y)
            points.append([x, y])
        points = sorted(points, key=lambda k: [k[0]])
        return points

    def distance(self, a, b): #expects 2 lists of an x and y coord
        return ( ((b[0] - a[0])**2) + ((b[1] - a[1])**2) )**0.5

    def edgecase3(self, pts): # case when there are 3 left in the list, simply use brute force
        min_dist = self.distance(pts[0], pts[1])
        min_dist = min(min_dist, self.distance(pts[0], pts[2]))
        min_dist = min(min_dist, self.distance(pts[1], pts[2]))
        return min_dist

    def closest2(self, points):
        return self.recurse(points)

    def recurse(self, points):

        #Base cases:

        if len(points) == 2:
            self.checkmins(self.distance(points[0], points[1]))
            return self.distance(points[0], points[1])

        if len(points) == 3:
            self.checkmins(self.edgecase3(points))
            return self.edgecase3(points)

        #Recursive case:

        mid = len(points) // 2

        min_left = self.recurse(points[:mid])
        
        min_right = self.recurse(points[mid:])

        current_min = min(min_left, min_right)

        #final_min = self.checkrunway(points, current_min)

        return current_min

    def checkrunway(self, points, closest_dist): #closest dist will be width of runway
        return "UNFINISHED"
    
    def checkmins(self, newdist): 
        if len(self.mins) == 0:
           self.mins.append(newdist)

        elif len(self.mins) == 1:
            if newdist < self.mins[0]:
                self.minsmins = [newdist, self.mins[0]]
            else:
                self.mins.append(newdist)

        elif newdist < self.mins[0]:
            self.mins = [newdist, self.mins[0]]

        elif newdist < self.mins[1]:
            self.mins[1] = newdist

        return self.mins