# Ryan Grayson
'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
'''
def numDecodings(s):
    l = len(s)
    nums = []
    #convert to list
    for c in s:
        nums.append(int(c))
    #ensure encoding is valid
    if s[0] == '0':
        return 0
    for i in range(1, l):
        if s[i] == '0' and s[i-1] != '1' and s[i-1] != '2':
            return 0
    # dp
    mem = [1] * (l+1)
    for i in range(1, len(s)):
        if s[i] == '0':
            mem[i+1] = mem[i-1]
            
        elif s[i-1] == '0':
            mem[i+1] = mem[i]
            
        elif s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) <= 6):
            if i-2 < 0 or s[i-2] == '0':
                mem[i+1] = mem[i] + 1
            else:
                mem[i+1] = mem[i-1] + mem[i]
                
        else:
            mem[i+1] = mem[i]

    print("s:", end='        | ')
    for c in s:
        print(c, end='  | ')
    print()
    print("------" * l)
    print("mem:", end=' | ')
    for n in mem:
        print(str(n), end="")
        if n < 10:
            print(' ', end='')
        print(end= ' | ')

    return mem[l]

r = numDecodings("10222220202721110727")
print()
print()
print("answer: " + str(r))