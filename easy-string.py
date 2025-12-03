
"""
Question Link : https://www.geeksforgeeks.org/problems/easy-string2212/1
Question Name : easy-string
"""

class Solution:

    def transform(self, S):
        # code here
        S=S+'1'
        res = ''
        count=0
        # print(S)
        for i in range(0 , len(S)-1):
            # print(i)
            first = S[i].lower()
            second = S[i+1].lower()
            if first == second :
                count+=1
            else:
                res += str(count+1)
                res +=first
                count=0
                
        
        
        
        return res