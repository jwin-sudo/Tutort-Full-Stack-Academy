'''
Q3. Given an sorted array A of size N. Find number of elements which are less than or equal to given
element X.
Example 1:
Input:
N=6
A[] = {1, 2, 4, 5, 8, 10} X=9
Output:
5
Example 2:
Input:
N=7
A[] = {1, 2, 2, 2, 5, 7, 9} X=2
Output:
4
'''

def findNumOfElements(arr, x):
 counter = 0

 for i in range(0, len(arr)-1, 1):
  if arr[i] <= x:
   counter = counter + 1
 return counter


counter = findNumOfElements([1, 2, 4, 5, 8, 10],9)
print(counter)