#!/usr/local/bin/python3
# Given an expression with numbers, brackets and operators. But in this task only brackets are important. Brackets can be one of three types -- "{}" "()" "[]". Brackets are determine the scope or restricted some expression. So each if was opened, then must be closed with the same type. The scopes of brackets must not intersected. You should to make a decision correct an expression or not. Don't care about operators and operands.
# Input: An expression with different of types brackets.
# Output: A boolean. Correct an expression or not.

def checkio(data):
    BRACKETS  = {'{':1, '}':-1,
                 '[':2, ']':-2,
                 '(':3, ')':-3}
    stack = []
    for c in data:
        if c in ['{', '[', '(']:
            stack.append(c)
        elif c in ['}', ']', ')']:
            if len(stack) == 0:
                return False
            open_c = stack.pop()
            if BRACKETS[open_c] + BRACKETS[c] != 0:
                return False
        else:
            pass

    return False if stack else True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"


