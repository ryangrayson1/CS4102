# CS4102 Spring 2022 -- Unit C Programming
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
import math

class SeamCarving:
    def __init__(self):
        return

    colors = []
    energies = []
    seam_xs = []
    mem = []
    r = 0 # rows
    c = 0 # cols

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        self.colors = image
        self.r = len(image)
        self.c = len(image[0])

        # Initialize all energies
        for j in range(self.r):
            self.energies.append([])
            for i in range(self.c):
                self.energies[j].append(self.energy(j, i))

        #getting energy sum for whole first column as placeholder for mem
        nrg1 = 0
        for f in range(self.r):
            nrg1 += self.energies[f][0]

        # initialize mem
        for j in range(self.r):
            self.mem.append([])
            for i in range(self.c):
                self.mem[j].append(nrg1)

        # set first row to actual values
        for i in range(self.c):
            self.mem[0][i] = self.energies[0][i]
        
        return self.dp()

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam_xs
    

    # Find the lowest energy seam
    def dp(self):
        for j in range(1, self.r):

            for i in range(self.c):
                #calc the lowest possible energy seam up to this point for the current column
                if i == 0:
                    min_prev_energy = min( self.mem[j-1][i], self.mem[j-1][i+1] )
                elif i == self.c - 1:
                    min_prev_energy = min( self.mem[j-1][i-1], self.mem[j-1][i] )
                else:
                    min_prev_energy = min( self.mem[j-1][i-1], self.mem[j-1][i], self.mem[j-1][i+1] )

                self.mem[j][i] = min_prev_energy + self.energies[j][i]

        # finally calculate lowest energy sum for seam based on last row of mem
        low_nrg = self.mem[self.r-1][0]
        low_col = 0
        for i in range(1, self.c):
            if self.mem[self.r-1][i] < low_nrg:
                low_nrg = self.mem[self.r-1][i]
                low_col = i


        # then backtrack to find the seam
        backtrace = []
        backtrace.append(low_col)
        for j in range(self.r - 2, -1, -1):
            #left edge
            if backtrace[-1] == 0:
                nextx = 0
                if self.mem[j][1] < self.mem[j][0]:
                    nextx = 1
            #right edge
            elif backtrace[-1] == self.c - 1:
                nextx = self.c - 2
                if self.mem[j][self.c - 1] < self.mem[j][self.c - 2]:
                    nextx = self.c - 1
            else:
                nextx = backtrace[-1] - 1
                if self.mem[j][backtrace[-1]] < self.mem[j][nextx]:
                    nextx = backtrace[-1]
                if self.mem[j][backtrace[-1] + 1] < self.mem[j][nextx]:
                    nextx = backtrace[-1] + 1

            backtrace.append(nextx)

        self.seam_xs = list(reversed(backtrace))
        return low_nrg

    # @return the difference value between 2 pixels
    def difference(self, j1, i1, j2, i2):
        r = (self.colors[j2][i2][0] - self.colors[j1][i1][0])**2
        g = (self.colors[j2][i2][1] - self.colors[j1][i1][1])**2
        b = (self.colors[j2][i2][2] - self.colors[j1][i1][2])**2
        return math.sqrt(r + g + b)

    # @return the energy of the pixel at position (j, i)
    def energy(self, j, i):
        jstart = j - 1
        jend = j + 1
        istart = i - 1
        iend = i + 1
        if j == 0:
            jstart += 1
        if i == 0:
            istart += 1
        if j == len(self.colors) - 1:
            jend -= 1
        if i == len(self.colors[0]) - 1:
            iend -= 1
        adj = (jend - jstart + 1) * (iend - istart + 1) - 1
        sum = 0.0
        for b in range(jstart, jend+1):
            for a in range(istart, iend+1):
                if b != j or a != i:
                    sum += self.difference(j, i, b, a)

        return sum / adj