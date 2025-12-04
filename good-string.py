"""
Question Link : https://www.geeksforgeeks.org/problems/good-string5712/1
Question Name : Good String
"""

class Solution:

    def isGoodString(self, s):
        # code here
        
        if len(s)==1:
            return 'YES'
        
        first = 0
        second = 1
        
        while first < len(s) and second < len(s):
            if s[first] =='a' and s[second] =='z':
                first+=1
                second+=1
                continue
            
            if s[first] =='z' and s[second] =='a':
                first+=1
                second+=1
                continue
            
            if abs ( ord(s[first] ) - ord(s[second])  ) == 1 :
                first+=1
                second+=1
            else:
                return 'NO'
                
        return 'YES'