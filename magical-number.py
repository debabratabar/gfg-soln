
"""
Question Link : https://www.geeksforgeeks.org/problems/magical-number-1587115620/1
Question Name : magical-number
"""


class Solution:
    def findMagicalNumber(self, arr):
        # code here
        
        for i in range(0 , len(arr)):
            if arr[i] == i:
                return i
                
        return -1