'''Q1. Given an array of N integers. Your task is to print the sum of all of the integers.

Example 1: Input:
4
1234 Output:
10
Example 2: Input:
6
5 8 3 10 22 45 Output:
93
'''

def totalSum(n):
 arr = []
 sum = 0
 i = 0
 
 while i < n:
  val = input("Enter a number: ")
  arr.append(int(val))
  i = i+1

  if i == n:
   break
 
 for i in range(0, len(arr), 1):
  sum = sum + arr[i]

 return sum

sum = totalSum(4)
print(sum)


