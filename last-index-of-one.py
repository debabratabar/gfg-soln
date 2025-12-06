"""
Question Link : https://www.geeksforgeeks.org/problems/last-index-of-15847/1
Question Name : Last index of One

"""

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        idx =-1
        
        for i in range(0 , len(s)):
            if s[i] =='1':
                idx = i
                
                
        return idx
        