#Problem 9 - Special Pythagorean Triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b <c , for which,
        a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

def pythagoreanTriplet(total):
    special_triangle = None
    a, b = 1, 2
    while True:
        c = (a**2 + b**2)**(1/2) #find c from a^2 + b^2 = c^2
        if a + b + c == total: #check if the sum of three is equal to the required total
            return (a, b, int(c))
        a += 1 
        if a == b:
            b += 1
            a = 1

start = time.time() #time is set
print(pythagoreanTriplet(10000))
end = time.time() #time is set again
print(end-start) #to find how much time does it takes to calculate

