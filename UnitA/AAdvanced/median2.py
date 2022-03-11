import math
salh = [100, 200, 300, 501, 700]
salm = [150, 400, 600, 800, 920] #expected 450.5

def median2(sals1, sals2):

    start1 = 0
    end1 = len(sals1) - 1
    start2 = 0
    end2 = len(sals2) - 1

    while end1 != start1 and end2 != start2:
        if (end1 - start1) % 2 != 0: #even case
            mid1 = (sals1[(end1 + start1) // 2] + sals1[(end1 + start1) // 2 + 1]) / 2
            even1 = True
        else: #odd case
            mid1 = sals1[(end1 - start1) // 2]
            even1 = False

        if (end2 - start2) % 2 != 0: #even case
            mid2 = (sals2[(end2 + start2) // 2] + sals2[(end2 + start2) // 2 + 1]) / 2
            even2 = True
        else: #odd case
            mid2 = sals2[(end2 + start2) // 2]
            even2 = False

        if mid1 == mid2:
            return mid1
        elif mid1 > mid2:
            end1 = (end1 + start1) // 2
            if even2:
                start2 = (end2 + start2) // 2 + 1
            else:
                start2 = (end2 + start2) // 2
        else:
            end2 = (end2 + start2) // 2
            if even1:
                start1 = (end1 + start1) // 2 + 1
            else:
                start1 = (end1 + start1) // 2

    return (sals1[start1] + sals2[start2]) / 2

print("result: ")
print(median2(salh, salm))

            
        


