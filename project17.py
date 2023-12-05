#Problem 17 - Number Letter Counts
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example,
    342 (three hundred and forty-two) contains 23 letters and 
    115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

num = 1000

def numLetterCount(n):
    nums = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
            7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve",
            13:"thirteen", 14:"forteen", 15:"fifteen", 16:"sixteen",
            17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty",
            30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",
            80:"eighty", 90:"ninety"}
    a, letter = 1, ""
    while a <= n:
        if a < 20:
            letter += nums[a]
        elif a < 100:
            letter += nums[a-a%10] + nums[a%10]
        elif a < 1000:
            if a%100 == 0:
                letter += nums[a//100] + "hundred"
            else:
                if a%100 in nums:
                    letter += nums[a//100] + "hundredand" + nums[a%100]
                else:
                    letter += nums[a//100] + "hundredand" + nums[a%100-a%10] + nums[a%10]
        else:
            letter += "onethousand"
        a += 1
    
    return len(letter), letter

lb, b = numLetterCount(num)
print("Total letters used:", lb)


##def num_to_words(num):
##    def func(x):
##        b = ""
##        if x < 20:
##            b += ones[x]
##        elif x < 100:
##            b += tens[x-x%10] + ones[x%10]
##        return b
##    a = ""
##    ones = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
##            8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
##            14:"forteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
##            19:"nineteen"}
##    tens = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
##            70:"seventy", 80:"eighty", 90:"ninety"}
##    for x in range(1,num+1):
##        if x < 100:
##            a += func(x)
##        elif x < 1000 and x >= 100:
##            if x % 100 == 0:
##                a += ones[x//100] + "hundred"
##            else:
##                a += ones[x//100] + "hundredand" + func(x%100)
##        else:
##            a += "onethousand"
##
##    return len(a), a
##
##
##la, a = num_to_words(num)    
##print("Total letters used:", la)



    
