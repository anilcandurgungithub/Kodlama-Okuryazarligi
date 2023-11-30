#https://projecteuler.net/problem=1
"""
Multiples of 3 or 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

total = 0
for x in range(1,1000): 
    if x % 3 == 0 or x % 5 == 0: # the numbers between 1-1000 are checked if they fit the rule
        total += x # if they fit the rule they are added to the total

print(total)


aim_list = [] # to reach every single item this ethod can be used
for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0:
        aim_list.append(x) # each item that fits are added to the list

print(sum(aim_list)) # sum of all of them is printed
