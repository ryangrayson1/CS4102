# cache replacement problem
# goal: minimize number of cache misses

#finds first occurrence or -1
def check_ap(access_pattern, start, elem):
    for i in range(start, len(access_pattern)):
        if access_pattern[i] == elem:
            return i
    return -1

def run_cache(access_pattern, k): #k is the cache size
    cache = []
    for i in range(k):
        cache.append(access_pattern[i])
    
    misses = 0
    for i, e in enumerate(access_pattern):
        if e not in cache:
            misses += 1
            mx = [i+1, 0]
            already_updated = False
            for c in range(k):
                this_i = check_ap(access_pattern, i, cache[c])
                if this_i == -1:
                    cache[c] = e
                    already_updated = True
                    break
                if this_i > mx[0]:
                    mx[0] = this_i
                    mx[1] = c

            if not already_updated:
                cache[mx[1]] = e

        print("after " + str(i) + ": " + str(access_pattern[i]))
        print("cache: ", end="")
        for l in cache:
            print(l, end=' | ')
        print()
    return misses

print(run_cache(['A', 'B', 'C', 'D', 'A', 'D', 'E', 'A', 'D', 'B', 'A', 'E', 'C', 'E', 'A'], 3))