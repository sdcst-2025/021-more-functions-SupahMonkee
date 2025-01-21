#!python3
"""
##### Problem 2
Create a function that determines if a triangle is acute, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

import math, statistics

def triangle(l1,l2,l3):
    numlist = [l1,l2,l3]
    a = min(numlist)
    b = statistics.median(numlist)
    c = max(numlist)
    if a + b < c:
        triangletype = 0
    else:
        if (a**2)+(b**2) > (c**2):
            triangletype = 1
        if (a**2)+(b**2) == (c**2):
            triangletype = 2
        if (a**2)+(b**2) < (c**2):
            triangletype = 3
    return triangletype

#done!

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
