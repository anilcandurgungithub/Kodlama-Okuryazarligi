#Problem 15 - Lattice Paths
"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

def calculateLattice(grid): #by using permutation, we can calculate
    a = 1 
    for x in range(1, grid+1):
        a = a*((grid+x)/x)
    return a


grid = 20
print(calculateLattice(grid))
