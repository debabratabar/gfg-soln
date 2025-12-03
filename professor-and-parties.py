"""
Question Link : https://www.geeksforgeeks.org/problems/professor-and-parties2000/1
Question Name : Professor and Parties

"""

class Solution:
    def PartyType(self, arr):
        # Your code goes here
        
        max_val = float('-inf')
        
        for i in arr:
            if i > max_val:
                max_val = i 
                
        
        res = [0] * max_val
        
        for i in arr:
            res[i-1]+=1
            
            if res[i-1] > 1 :
                return 'true'
                
            # print(res)
                
        return 'false'