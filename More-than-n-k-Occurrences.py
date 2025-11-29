"""
Question Link : https://www.geeksforgeeks.org/problems/count-element-occurences/1
Question Name : More than n/k Occurrences 

"""


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        #Your code here
        ans = {}
        res=0
        
        for i in arr:
            
            if i not in ans:
                ans[i] = 1
            else:
                val = ans[i]
                ans[i] = val+1
        
        
        for key , val in ans.items():
            if val > int (len(arr) / k ):
                res+=1
                
                
        return res