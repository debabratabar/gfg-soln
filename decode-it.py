
"""
Question Link : https://www.geeksforgeeks.org/problems/decode-it1646/1
Question Name : decode-it
"""

#User function Template for python3

class Solution:

    def decodeIt(self, Str, k):
        # code here
        
        subS = ''
        res = {}
        for i in Str:
            if i.isdigit():
                res[subS] = int(i)
                subS=''
                
            else:
                subS+=i
                
                
        ans=''
        # print(res)
        
        
        for key,value in res.items():
            ans = (ans +key) * value
            
        # print(ans)
        
        
        return ans[k-1]
        
        # jonjonsnowsnowsnow
        # r 
        # s
            
        