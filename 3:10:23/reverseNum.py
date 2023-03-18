'''

Reverse 541 to 145 int

'''


def reverseNum(n):
    output = 0
    while n > 0:
        remainder = n % 10
        n = n//10
        output = output * 10 + remainder
    return (output)


reverse = reverseNum(541)
print(reverse)
