#Problem 3 - Largest Prime Factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def prime_factor(num):
    prime_list = []
    factor = 2
    while True:
        if num == 1: #when the number hits 1 eventually, stop the program
            break
        if num % factor == 0: 
            prime_list.append(factor) 
            num //= factor #divide the num to understand when to stop
        else:
            factor += 1
            
    return prime_list


num = 600851475143
print(f"Largest prime factor of {num} is {prime_factor(num)[-1]}.")
