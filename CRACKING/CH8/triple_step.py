def staircase_ways(n): # O(3^n)
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
               
    return staircase_ways(n-1) + staircase_ways(n-2) + staircase_ways(n-3)

def staircase_helper(n): # O(N) with memoization (top-down programming)
    memo = [0] * (n + 1) # be careful about indexing
    return staircase_ways_memo(n, memo) # always remember to return in your functions

def staircase_ways_memo(n, memo):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    if memo[n] > 0:
        return memo[n]
    
    memo[n] = staircase_ways_memo(n-1, memo) + staircase_ways_memo(n-2, memo) + staircase_ways_memo(n-3, memo)
    return memo[n]

print(staircase_helper(4))

