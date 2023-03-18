'''
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

'''


def happyNumber(n):
    seen = set()
    while n:
        sum_of_digit = 0
        for digit in str(n):
            sum_of_digit = sum_of_digit + int(digit)**2
            n = sum_of_digit
        if n in seen:
            return False
        elif n == 1:
            return True
        seen.add(n)


result = happyNumber(19)
print(result)
