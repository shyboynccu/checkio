#/usr/local/bin/python3
# Let F(n) is a function from natural number. This function is equal the sum of all numbers in combinations with length from 1 to n in the set of natural numbers (1...n). For example:
#     F(1) = 1
#     F(2) = ((1)+(2))+((1+2))
#     F(3) = ((1)+(2)+(3))+((1+2)+(1+3)+(2+3))+((1+2+3))

# Functions G(n) is the sum of F(s) where s = 1...n.
#     G(1) = F(1)
#     G(2) = F(1) + F(2)
#     G(3) = F(1) + F(2) + F(3)

# You should to calculate G(n) for given n.
# Input: A integer.
# Output: A integer.

f_cache = [0, 1]
def F(n):
    global f_cache
    if len(f_cache) > n:
        return f_cache[n]

    x = (1 << (n-1)) - 1 # count of subsets of n-1
    y = F(n-1)
    value = 2*y + n*(x+1)
    f_cache.append(value)
    return value

def G(n):
    sum = 0
    for i in range(1, n+1):
        sum += F(i)
    return sum

def checkio(data):
    return G(data)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "First"
    assert checkio(2) == 7, "Second"
    assert checkio(3) == 31, "Third"
    assert checkio(4) == 111, "Fourth"
