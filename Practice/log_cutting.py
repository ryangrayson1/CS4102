# log cutting DP problem

#inputs: log[0] is cost of length 1 log, log[1] is cost of length 2 log, etc...
log1 = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
log2 = [1, 18, 24, 36, 50, 50]
log3 = [1, 5, 8, 9, 10, 17, 17, 20] #geeksforgeeks: 22
log4 = [3, 5, 8, 9, 10, 17, 17, 20] #geeksforgeeks: 24

def cut_log(prices):
    n = len(prices)
    mem = [0] * (n+1)

    for i in range(1, n+1):
        mx = prices[i-1]
        for j in range(i-1):
            mx = max(mx, prices[j] + mem[i-j-1])
        mem[i] = mx
    return mem[n]

print(log1)
print(cut_log(log1))
print()
print(log2)
print(cut_log(log2))
print()
print(log3)
print(cut_log(log3))
print()
print(log4)
print(cut_log(log4))
print()
