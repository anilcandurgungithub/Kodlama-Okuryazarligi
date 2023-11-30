#Problem 4 - Largest Palindrome Product
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99
.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largestPalindrome(num1, num2):
    largestPalNum, n1, n2 = 0, 0, 0
    for x in range(10**(len(str(num1))-1),num1):
        for y in range(10**(len(str(num2))-1),num2): # all the possibilities will be calculated
            t = x*y
            if str(t) == str(t)[::-1] and largestPalNum < t: # checking if the number is palindromic and bigger then the previous matching number
                largestPalNum = t
                n1, n2 = x, y
    return largestPalNum, n1, n2

num1, num2 = 999, 999
print("The largest palindromic number is %s = %s x %s"%largestPalindrome(num1, num2))


        
