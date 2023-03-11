'''
Bonus Question
Given an array of even size N, task is to find minimum value that can be added to an element so that array become balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of right half.
Example 1:
Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 1
Explanation: Sumoffirst2elementsis1+5 = 6, Sumoflast2elementsis3+2 = 5,
To make the array balanced you can add 1.
'''


def balance(n):
    left_side = n[0] + n[1]
    right_side = n[len(n)-1] + n[len(n)-2]

    if left_side > right_side:
        difference = left_side - right_side
        return 'To make the array balanced you can add ' + str(difference) + ' to the right side'

    if right_side > left_side:
        difference = right_side - left_side
        return 'To make the array balanced you can add ' + str(difference) + ' to the left side'


balance = balance([1, 5, 3, 2])
print(balance)
