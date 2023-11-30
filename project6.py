#Problem 6 - Sum Square Difference
"""
The sum of the squares of the first ten natural numbers is,
        1^2+2^2+...+10^2 = 358
The square of the sum of the first ten natural numbers is,
        (1+2+...+10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sumSquareDiff(num):
    var1, var2 = 0, 0

    for x in range(num):
        var1 += (x+1)**2

    term = (num - 1)+1 # calculating how much terms are there
    mid = (num + 1)/2 # calculating the middle point
    var2 = (term*mid)**2 #multiplying term num. and middle term gives the sum of the set

    return int(var1), int(var2), int(var2 - var1)



num = 100
result = sumSquareDiff(num)
print(f"""1^2 + 2^2 + ... + {num}^2 = {result[0]}
(1 + 2 + ... + {num})^2 = {result[1]}

{result[0]} - {result[1]} = {result[2]}""")

    
