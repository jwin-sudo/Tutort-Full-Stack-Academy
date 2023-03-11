'''
Q6. Given an array of size N and you have to tell whether the array is perfect or not. An array is said to be perfect if it's reverse array matches the original array. If the array is perfect then print "PERFECT" else print "NOT PERFECT".
Example 1:
Input : Arr[] = {1, 2, 3, 2, 1}
Output : PERFECT
Explanation:
Here we can see we have [1, 2, 3, 2, 1] if we reverse it we can find [1, 2, 3, 2, 1] which is the same as before.
So, the answer is PERFECT.
Example 2:
Input : Arr[] = {1, 2, 3, 4, 5} Output : NOT PERFECT
'''
def perfectArray(arr):
 if arr[0::1] == arr[::-1]:
  return 'PERFECT'
 else:
  return 'NOT PERFECT'
perfect = perfectArray([1, 2, 3, 4, 5])
print(perfect)