
'''
Example 2:
Input:
N = 6
arr[] = {1, 2, 1, 2, 1, 3} Output: 2 Explanation:
Sum of first 3 elements is 1 + 2 + 1 = 4, Sum of last three elements is 2 + 1 + 3 = 6, To make the array balanced you can add 2.
'''


def balance(n):
    left_side = n[0] + n[1] + n[2]
    right_side = n[len(n)-1] + n[len(n)-2] + n[len(n)-3]

    if left_side > right_side:
        difference = left_side - right_side
        return 'To make the array balanced you can add ' + str(difference) + ' to the right side'

    if right_side > left_side:
        difference = right_side - left_side
        return 'To make the array balanced you can add ' + str(difference) + ' to the left side'


balance = balance([1, 2, 1, 2, 1, 3])
print(balance)
