#Problem 10 - Summation of Primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sumPrime(num):
    prime, val = [2], 3
    while val <= num: 
        check = True
        for x in prime: #divide the value by all the prime numbers found,
            if val % x == 0: #if they coul dividable by them,
                check = False #that simply means they are not prime
                break
        if check: #if val is not dividable by any primes,
            prime.append(val) #that means it is prime.
        val += 2

    return sum(prime),prime





print(sumPrime(2000000))
        
