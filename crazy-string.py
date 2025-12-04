"""
Question Link : https://www.geeksforgeeks.org/problems/crazy-string1157/1
Question Name : Crazy String

"""

class Solution:

    def getCrazy(self, S):
        # code here
        
        chck = S[0].islower()
        
        S+='1'
        res = S[0]
        
        if chck:
            for i in range(1,len(S)-1):
                if i%2 !=0:
                    res += S[i].upper()
                else:
                    res += S[i].lower()
                    
            
                
        else:
            
            for i in range(1,len(S)-1):
                if i%2 !=0:
                    res += S[i].lower()
                else:
                    res += S[i].upper()
            
        return res