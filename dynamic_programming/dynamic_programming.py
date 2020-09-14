'''
Source: https://www.youtube.com/watch?v=f2xi3c1S95M
Minimum staps to minimize n to 1
Given an int n, return the min steps to minimize n to 1

Available steps are:
- Decrement n by 1
- If n is divisible by 2, then divide n by 2.
- If n is divisible by 3, then divide n by 3.

Examples:
10 => 3 steps (10 => 9 => 3 => 1)
15 => 4 steps (15 => 5 => 4 => 2 => 1)
'''

import sys

def get_min_steps(n):
    if n == 1:
        return 0

    result = get_min_steps(n-1)

    if n % 2 == 0:
        result = min(result, get_min_steps(int(n/2)))

    if n % 3 == 0:
        result = min(result, get_min_steps(int(n/3)))

    return result + 1


def get_min_steps_memo(n, memo):
    if n == 1:
        return 0

    if n in memo:
        return memo[n]

    result = get_min_steps_memo(n-1, memo)

    if n % 2 == 0:
        result = min(result, get_min_steps_memo(int(n/2), memo))

    if n % 3 == 0:
        result = min(result, get_min_steps_memo(int(n/3), memo))

    memo[n] = result + 1

    return memo[n]

def get_min_steps_tab(n):
    table = [n] * (n + 1) # initialize array with default val. n; essentially the max int value for this problem
    table[1] = 0

    for i in range(n):
        table[i] = min(table[i+1], table[i] + 1)
        if i * 2 <= n:
            table[i*2] = min(table[i] + 1, table[i*2])
        if i * 3 <= n:
            table[i*3] = min(table[i] + 1, table[i*3])
    return table[n]

if __name__ == '__main__':
    print("recursive:")
    print(get_min_steps(6))
    print(get_min_steps(100))
    # print(get_min_steps(1000)) # crash!

    print("memoization:")
    memo = {}
    print(get_min_steps_memo(6, memo))
    print(get_min_steps_memo(100, memo))
    print(get_min_steps_memo(1000, memo))
    # print(get_min_steps_memo(10000, memo)) #crash! instead of top-down approach, try tabulation (bottom up approach)

    print("tabulation:")
    print(get_min_steps_tab(6))
    print(get_min_steps_tab(100))
    print(get_min_steps_tab(1000))
    print(get_min_steps_tab(10000))

