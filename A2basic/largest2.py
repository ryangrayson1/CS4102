# Ryan Grayson
# Divide and conquer algorithm to find the largest 2 elements of a list
# 2/10/2022

def largest2(L, start, end): 
    if start - end == 1:
        if L[start] > L[end]:
            return [L[start], L[end]]
        else:
            return [L[end], L[start]]
    
    mid = (start + end) // 2 

    if start == end:
        return [L[start], -2147483648]
    
    largest2r = largest2(L, mid + 1, end)
    largest2l = largest2(L, start, mid)
    
    if largest2r[0] > largest2l[0]:
        if largest2r[1] > largest2l[0]:
            return [largest2r[0], largest2r[1]]
        else:
            return [largest2r[0], largest2l[0]]
    
    else:
        if largest2l[1] > largest2r[0]:
            return [largest2l[0], largest2l[1]]
        else:
            return [largest2l[0], largest2r[0]]

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [238,8320,92,4,0,1,-3,5,1000,-300]
arr3 = [0,-100,100,-300,700,1,2,3,4]
arr4 = [0,1]
arr5 = [-10]
arr6 = [1,2,3]

print(arr1)
print("Largest 2 elements: " + str(largest2(arr1, 0, 9)))
print()
print(arr2)
print("Largest 2 elements: " + str(largest2(arr2, 0, 9)))
print()
print(arr3)
print("Largest 2 elements: " + str(largest2(arr3, 0, 8)))
print()
print(arr4)
print("Largest 2 elements: " + str(largest2(arr4, 0, 1)))
print()
print(arr5)
print("Largest 2 elements: " + str(largest2(arr5, 0, 0)))
print()
print(arr6)
print("Largest 2 elements: " + str(largest2(arr6, 0, 2)))
print()