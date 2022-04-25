from __future__ import print_function
import time
from rooks import MaxRooks

fp = open("test2.txt", 'r')
fulllines = fp.readlines()
lines = []
for line in fulllines:
    lines.append(line.strip())

start = time.time()
mr = MaxRooks()
result = mr.compute(lines)
end = time.time()
print("Max non-interfering Rooks: " + str(result))
print("time: "+ str(end-start))
