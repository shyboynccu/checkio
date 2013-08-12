#/usr/local/bin/python3
# To write a nice song Sophie needs to come up with a perfect rhythm according to the Euclidean algorithm. In order to calculate it he will need the greatest common divisor of two numbers. Write a function that will calculate a greatest common divisor of two numbers.
# Example:
# Input: A list of two integers.
# Output: The greatest common divisor. A integer.
def checkio(data):
    a, b = data
    if b == 0:
        return a
    else:
        return checkio((b, a % b))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First example"
    assert checkio((14, 21)) == 7, "Second example"
    assert checkio((13, 11)) == 1, "Third example"
    