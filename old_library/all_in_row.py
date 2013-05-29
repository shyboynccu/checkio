#!/usr/local/bin/python3
# There is a list that contains integers, list of integers or nested lists. Put all integer values in one list.
# Input data: A nested list or simple list.
# Output data: One-dimensional list.
def checkio(data):

    #replace this for solution
    answer = []
    for item in data[:]:
        if type(item) == int:
            answer.append(item)
        else:
            # item is list
            answer += checkio(item)

    return answer


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3]) == [1, 2, 3], 'First example'
    assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second example'
    assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) \
           == [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'
