'''
Q8. Given an array of N distinct elements, the task is to find all elements in array except two greatest elements in sorted order.
Example 1:
Input :
a[] = {2, 8, 7, 1, 5}
Output :
125
Explanation :
The output three elements have two or more greater elements.
Example 2:
Input :
a[] = {7, -2, 3, 4, 9, -1}
Output :
-2 -1 3 4
'''

def findAll(arr):
 arr.sort()
 new_arr = arr[0:len(arr)-2:1]
 for i in range(0, len(new_arr), 1):
  print(new_arr[i])

findAll([2, 8, 7, 1, 5])

