'''
Q2. Given an array A[] of N integers and an index Key. Your task is to print the element present at index key in the array.
Example 1: Input:
5 2
10 20 30 40 50 Output:
30
Example 2:
Input:
7 4
10 20 30 40 50 60 70 Output:
50
'''

def findIndex(size, key):
 i = 0
 arr = []
 while i < size:
  val = input("Enter a number: ")
  arr.append(int(val))
  i = i + 1
  if i == size:
   break
 
 for i in range(0, len(arr),1):
  if i == key:
   return arr[i]

ValueOfKey = findIndex(7,4)
print(ValueOfKey)
