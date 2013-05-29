#!/usr/local/bin/python3
# Write a module that enables the robots to easily recall their passwords through codes when they return home.
# 
# Input: Two lists. The first list with four lines contain the Robot's cipher grille. The next list with four lines contain the square with the ciphered password. All the symbols in the square are lowercase Latin letters.
# 
# Output: Password

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    grille, template = data
    text = ''
    mask = [(x,y) for x in range(4) for y in range(4) if grille[x][y] == 'X']
    for i in range(4):
        text += ''.join([template[x][y] for (x, y) in mask])
        mask = sorted([(y, 3-x) for (x,y) in mask])
        
    return text

#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        ['X...',
         '..X.',
         'X..X',
         '....'],
        ['itdf',
         'gdce',
         'aton',
         'qrdi']]) == 'icantforgetiddqd', 'First example'

    assert checkio([
        ['....',
         'X..X',
         '.X..',
         '...X'],
        ['xhwc',
         'rsqx',
         'xqzz',
         'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'