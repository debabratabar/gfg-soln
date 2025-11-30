
"""
Question Link : https://www.geeksforgeeks.org/problems/count-of-distinct-substrings/1
Question Name : count-of-distinct-substrigs
"""

class Solution:
    def countSubs(self, s):
        # code here
        
        #  1. we can't use set as set.add() has o(n) , total comp --> O(n^3)
        # 2. we have to use dict and compare on the go for duplicates
        
        if len(s) ==1:
            return 1
        
        ans = {}
        cnt =0
        str = ''
        
        for i in range(0,len(s)+1):
            
            for j in range(0 , len(s)-i):
                str = s[j:i+j+1] 
                if str not in ans:
                    ans[str] = 1
                    cnt+=1
                    
            ans={}    
               
              
        return cnt
        
        
        