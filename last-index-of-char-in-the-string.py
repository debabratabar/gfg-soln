"""
Question Link : https://www.geeksforgeeks.org/problems/last-index-of-a-character-in-the-string4516/1
Question Name : Last index of a character in the string

"""

class Solution:
    def LastIndex(self, s, p):
        # code here
        idx=-1
        
        for i in range(0,len(s)):
            if p == s[i]:
                idx = i
                
        return idx