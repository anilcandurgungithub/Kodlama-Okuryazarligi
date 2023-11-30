#Problem 7 - 10001st Prime
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

def prime(num):
    prime_list, prime_num = [2], 3
    while len(prime_list) < num:
        is_prime = True
        for i in prime_list:
            if prime_num % i == 0: #checks if the number can be divided by the prime numbers
                is_prime = False
                break # if its not prime breaks the loop
        if is_prime:
            prime_list.append(prime_num)
        prime_num += 2

    return prime_list[-1]


which = 10
result = prime(which)
if str(which).endswith("1"):
    suf = "st"
elif str(which).endswith("2"):
    suf = "nd"
elif str(which).endswith("3"):
    suf = "rd"
else:
    suf = "th"
print(f"{which}{suf} prime number is {result}.")
