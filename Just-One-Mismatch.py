"""
Question Link : https://www.geeksforgeeks.org/problems/just-one-mismatch1714/1
Question Name : Just One Mismatch

"""

class Solution:
    def isStringExist (self, arr, N, S):
        # code here 
        
        cnt = 0 
        
        for i in arr:
            if len(S) == len(i):
                for j in range(0,len(i)):
                    if i[j] != S[j]:
                        cnt+=1
                        
                if cnt==1:
                    return True
                else:
                    cnt=0
                        
        
        # print(cnt)                
        
        # if cnt==1:
        #     return True 
            
        return False