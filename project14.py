#Problem 14 - Longest Collatz Sequence
"""
The following iterative sequence is defined for the set of positive integers:
            n -> n/2 (n is even)
            n -> 3n+1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
            13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def longestColatz(limit):
    longest, lengths, var = 0, {0:0}, 2
    while limit > var: #when hit the limit break the loop
        num = var
        count = 0
        while num > 1: #when arrived to 1, break the loop
            if num in lengths: #a shortcut not to calculate again,
                count += lengths[num] #if the number was already calculated
                break
            if num % 2 == 0:
                num = num//2
            else:
                num = 3*num+1
            count += 1
        lengths[var] = count #save the number of chains for the shortcut
        if count > lengths[longest]: #save the number which has the longest chain
            longest = var
        var += 1
        
                
    return longest, lengths

lo, le = longestColatz(1000000)
print(lo, le[lo])
