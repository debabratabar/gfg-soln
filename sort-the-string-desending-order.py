"""
Question Link : https://www.geeksforgeeks.org/problems/sort-the-string-in-descending-order3542/1
Question Name : Sort the string in descending order

"""

class Solution:
    def ReverseSort(self, s): 
        # code here
        s= sorted(s)
        res = s[-1::-1]
        
        
        return ''.join(res)