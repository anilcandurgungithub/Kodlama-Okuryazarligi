#Problem 5 - Smallest Multiple
"""
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1  to 20?
"""

def smallestMultiple(num):
    range_list = list(range(1, num+1))
    smallestMultiplier, dividing = 1, 2

    while dividing <= num+1: #stops when the count reaches the number asked
        check = False
        for divided in range(num):
            if range_list[divided] % dividing == 0:
                range_list[divided] //= dividing #divides all the dividable numbers in the list
                check = True
        
        if check:
            smallestMultiplier *= dividing
        else:
            dividing += 1 #if cannot divide by "dividing" var anymore add 1 and go on
    
    return smallestMultiplier


    
print(smallestMultiple(20))


















    
