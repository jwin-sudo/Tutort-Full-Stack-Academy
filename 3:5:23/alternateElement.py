'''
Q4. You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).
Example 1:
Input:
N=4
A[] = {1, 2, 3, 4} Output:
1 3
Example 2: Input:
N=5
A[] = {1, 2, 3, 4, 5} Output:
1 3 5
'''

def alternateElement(arr):
 for i in range(0, len(arr), 2):
  print(arr[i])

alternateElement([1, 2, 3, 4])