from __future__ import print_function
import time
from queens import MaxQueens

fp = open("test2.txt", 'r')
fulllines = fp.readlines()
lines = []
for line in fulllines:
    lines.append(line.strip())

start = time.time()
mr = MaxQueens()
result = mr.compute(lines)
end = time.time()
print("Max non-interfering Queens: " + str(result))
print("time: "+ str(end-start))
