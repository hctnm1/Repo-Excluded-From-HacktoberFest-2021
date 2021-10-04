/* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<          Question-> Find Unique        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.

Input format :
  
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
First line of each test case or query contains an integer 'N' representing the size of the array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
  
For each test case, print the unique element present in the array.
Output for every test case will be printed in a separate line.

Constraints :
  
1 <= t <= 10^2
0 <= N <= 10^3
Time Limit: 1 sec
  
Sample Input :
  
1
7
2 3 1 6 3 6 2

Sample Output :
  
1

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<      Solution Of Program         >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import sys
def findUnique(arr, n) :
    for i in range(n) :
        j = 0
        while j < n :
            if i != j :
                if arr[i] == arr[j] :
                    break
            j += 1
        if j == n : 
            return arr[i]
def takeInput() :
    n = int(input())
    if n == 0 :
        return list(), 0
    arr = list(map(int, input().rstrip().split(" "))) 
    return arr, n
t = int(input()) 
while t > 0 : 
    arr, n = takeInput()
    print(findUnique(arr, n)) 
    t -= 1
