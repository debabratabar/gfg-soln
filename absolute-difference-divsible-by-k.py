
"""
Question Link : https://www.geeksforgeeks.org/problems/absolute-difference-divisible-by-k/1
Question Name : absolute-difference-divsible-by-k
"""


#User function Template for python3

class Solution:
    def countPairs (self, n, arr, k):
        # code here
        
        cnt = 0
        
        rem = [] 
        
        for i in arr:
            rem.append(i%k)
            
        ans = [0] * k
        
        
        
        for i in rem:
            ans[i]+=1
            
        # print(ans) 
        
        for i in ans:
            cnt+= int(( i * (i-1))/2)
        
        
        
        return cnt
                