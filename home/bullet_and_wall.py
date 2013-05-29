#!/usr/local/bin/python3
# The wall is represented by two coordinates W1 (xw1, yw1) and W2 (xw2, yw2) on a coordinate plane. The bullet flies from point "A" (xa, ya), and the direction of its flight is given by the second point "B" (xb, yb). Determine whether the bullet hits the wall or not if gravity is not a factor. A != B.
#
# Input: Four lists with coordinates--each one is a list of x and y coordinates--W1, W2, A, B (Integers).
#
# Output: Whether the bullet hits the wall or not, aka True or False.

class TheWall:
    """Define the wall"""
    def __init__(self, w1, w2):
        # implement y = mx + b
        self.xw1, self.yw1 = w1
        self.xw2, self.yw2 = w2
        
    def find_point(self, x):
        if self.yw1 == self.yw2:
            # horizontal line
            return [x, self.yw1]
        elif self.xw1 == self.xw2:
            # vertical line
            return None
        else:
            delta_x_w12 = self.xw2 - self.xw1
            delta_y_w12 = self.yw2 - self.yw1
            
            delta_x_xw2 = x - self.xw2
            delta_y_xw2 = delta_y_w12*delta_x_xw2/delta_x_w12
            
            y = delta_y_xw2 + self.yw2
            
            return [x, y]
        
        
def step_increment(start, end):
    if start[0] == end[0]:
        step_x = 0
        step_y = 1 if end[1] > start[1] else -1
    else:
        step_x = 1 if end[0] > start[0] else -1
        step_y = (end[1]-start[1])*step_x/(end[0]-start[0])
    
    return step_x, step_y    

    
def checkio(data):

    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    
    lower_bound_x, upper_bound_x = sorted([xw1, xw2])
    lower_bound_y, upper_bound_y = sorted([yw1, yw2])
    
    wall = TheWall(data[0], data[1]) if xw2 >= xw1 else TheWall(data[1], data[0])
        
    step_x, step_y = step_increment(data[2], data[3])
    # print("step_x=%f, step_y=%f" % (step_x, step_y))
    if step_x == step_y == 0:
        # A == B
        return False
    else:
        x = xa
        y = ya
        
        distance = None
        while True:
            # Find next point in bullet path
            x += step_x
            y += step_y
            # print("Check point (%f, %f)" % (x, y))
            
            if (upper_bound_x >= x >= lower_bound_x and upper_bound_y >= y >= lower_bound_y):
                # find the correspoding coordinate on the wall
                wall_point = wall.find_point(x)
                if wall_point is None:
                    # wall is vertical
                    return True
                else:
                    wall_y = wall_point[1]
                    # print("Check wall point (%f, %f)" % (wall_point[0], wall_point[1]))
                    if distance is not None:
                        if (y - wall_y) * distance <= 0:
                            # cross the wall
                            return True
                    else:
                        distance = y - wall_y
                        if distance == 0:
                            return True

            if ((x > upper_bound_x and step_x > 0) or
                (x < lower_bound_x and step_x < 0) or
                (y > upper_bound_y and step_y > 0) or
                (y < lower_bound_y and step_y < 0)):
                return False
                

#Some hints
#You can search intersection point for lines
#Or look to rays geometry


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[9,7], [2,5], [5,3], [2,5]]) == True
    assert checkio([[10,2], [1,6], [7,5], [10,7]]) == False
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "1st example"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"
