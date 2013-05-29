#!/usr/local/bin/python3
# You are given a list of integer weights. You need to distribute these weights into two sets, such that the difference between the total weight of each set is as low as possible.
# 
# Input data: A list of the weights.
# 
# Output data: A number representing the lowest possible weight difference.
def checkio(data):
    cases = [(0, 0)]
    while data:
        this_item_weight = data.pop()
        new_cases = []
        for case in cases:
            new_cases.append((case[0] + this_item_weight, case[1]))
            new_cases.append((case[0], case[1] + this_item_weight))
        
        cases = new_cases

    best_case = min(cases, key = lambda pair: abs(pair[0] - pair[1]))                        

    return abs(best_case[0] - best_case[1])

#Some hints
#Your can use combinations if you want use bruteforce


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
