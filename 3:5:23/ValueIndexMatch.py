'''
Q5. Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).
Example 1:
Input:
N=5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here. Example 2:
Input:
N=1
Arr[] = {1}
Output: 1
Explanation: Here Arr[1] = 1 exists.
'''
def valueIndexMatch(arr):
 for i in range(0,len(arr), 1):
  if i+1 == arr[i]:
   return arr[i]

ans = valueIndexMatch([1])
print(ans)