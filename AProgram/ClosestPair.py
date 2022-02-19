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
        self.closest2(file_data)
        return self.mins

    #accepts the list of strings and returns a list of coordinate lists: [x, y] sorted by x coordinate
    def to_sorted_list(self, data, xy):
        points = []
        for line in data:
            x, y = line.split()
            x = float(x)
            y = float(y)
            points.append([x, y])
        if xy == 1:
            points = sorted(points, key=lambda k: k[1])
        else:
            points = sorted(points, key=lambda k: [k[0], k[1]])
        return points

    def distance(self, a, b): #expects 2 lists of an x and y coord
        return ( ((b[0] - a[0])**2) + ((b[1] - a[1])**2) )**0.5

    def edgecase3(self, pts): # case when there are 3 left in the list, simply use brute force
        min_dist = self.distance(pts[0], pts[1])
        min_dist = min(min_dist, self.distance(pts[0], pts[2]))
        min_dist = min(min_dist, self.distance(pts[1], pts[2]))
        return min_dist

    def closest2(self, points):
        srtdx = self.to_sorted_list(points, 0)
        srtdy = self.to_sorted_list(points, 1)
        return self.recurse(srtdx, srtdy)

    def recurse(self, points, y_sorted):

        #Base cases:
        if len(points) == 2:
            self.checkmins(self.distance(points[0], points[1]))
            return self.distance(points[0], points[1])

        if len(points) == 3:
            self.checkmins(self.edgecase3(points))
            return self.edgecase3(points)

        #Recursive case:
        mid = len(points) // 2 #midpoint for our split

        leftysort = []
        rightysort = []
        for i in range(len(points)): #divide the y lists in O(n)
            if y_sorted[i][0] < points[mid][0] or (y_sorted[i][0] == points[mid][0] and y_sorted[i][1] < points[mid][1] and len(leftysort) < mid):
                leftysort.append(y_sorted[i])
            else:
                rightysort.append(y_sorted[i])

        min_left = self.recurse(points[:mid], leftysort)
        
        min_right = self.recurse(points[mid:], rightysort)

        current_min = min(min_left, min_right)
        
        final_min = min(current_min, self.checkrunway(current_min, y_sorted, points[mid][0]))

        return final_min

    def checkrunway(self, closest_dist, y_sorted, cut): #closest dist will be width of runway
        runwaypts = []

        for i in range(len(y_sorted)):
            if y_sorted[i][0] >= cut - closest_dist and y_sorted[i][0] <= cut + closest_dist:
                runwaypts.append(y_sorted[i])
        
        if len(runwaypts) >= 2:
            runway_mins = [2100000000, 2100000000]
            rx1 = 2100000000
            rx2 = 2100000000
            r2x1 = 2100000000
            r2x2 = 2100000000

            for i in range(len(runwaypts)):
                for j in range( i + 1, min(i + 8, len(runwaypts))):
                    dst = self.distance(runwaypts[i], runwaypts[j]) 
                    res = self.checkmins2(dst, runway_mins)

                    if res[1] == 1:
                        rx1 = runwaypts[i][0]
                        rx2 = runwaypts[j][0]
                    elif res[1] == 2:
                        r2x1 = runwaypts[i][0]
                        r2x2 = runwaypts[j][0]
                    elif res[1] == 12:
                        r2x1 = rx1
                        r2x2 = rx2
                        rx1 = runwaypts[i][0]
                        rx2 = runwaypts[j][0]

                    runway_mins = res[0]

            if (rx1 < cut and rx2 >= cut) or (rx1 >= cut and rx2 < cut): # this would mean that this pair was not originally accounted for by the d & c
                self.checkmins(runway_mins[0])
            if (r2x1 < cut and r2x2 >= cut) or (r2x1 >= cut and r2x2 < cut):
                self.checkmins(runway_mins[1])

            return runway_mins[0]
        else:
            return closest_dist
    
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

    def checkmins2(self, newdist, the_mins): 
        x = 0 #no change of mins
        if len(the_mins) == 0:
            the_mins.append(newdist)
            x = 1 #first val

        elif len(the_mins) == 1:
            if newdist < the_mins[0]:
                the_mins = [newdist,the_mins[0]]
                x = 12 # first val and second val moved
            else:
                the_mins.append(newdist)
                x = 2 #just 2nd val moved

        elif newdist < the_mins[0]:
            the_mins = [newdist, the_mins[0]]
            x = 12 #both

        elif newdist < the_mins[1]:
            the_mins[1] = newdist
            x = 2 #just 2nd

        return [the_mins, x]