#!/usr/local/bin/python3
# An integer is said to be a palindrome if it is equal to its reverse in a string form. For example, 79197 and 324423 are palindromes. In this task you will be given an integer N. You must find the smallest integer M >= N such that M is a prime number and M is a palindrome. 
# Input: An integer.
# Output: A prime palindrome. An integer.
from math import sqrt, floor
def is_prime(number):
    for n in range(2, floor(sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True
    
def find_smallest_prime_palindrome(lower_bound, palindrome_list):
    for m in palindrome_list:
        if m >= lower_bound and is_prime(m):
            return m
    return None

    
def checkio(data):
    palindrome = [[],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [11, 22, 33, 44, 55, 66, 77, 88, 99]]
                  
    digit = 1
    while True:
        if digit < 3:
            m = find_smallest_prime_palindrome(data, palindrome[digit])
            if m:
                return m
        else:
            mid_palindrome_list = palindrome[digit-2]
            this_palindrome_list = []
            for n in range(1, 10):
                if mid_palindrome_list:
                    temp_list = [n*10**(digit-1) + x*10 + n for x in mid_palindrome_list]
                if data < pow(10, digit):
                    m = find_smallest_prime_palindrome(data, temp_list)
                    if m:
                        return m
                this_palindrome_list += temp_list
            palindrome.append(this_palindrome_list)      
        digit += 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(31) == 101, 'First example'
    assert checkio(130) == 131, 'Second example'
    assert checkio(131) == 131, 'Third example'