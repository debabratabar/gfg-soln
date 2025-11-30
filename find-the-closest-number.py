
"""
Question Link : https://www.geeksforgeeks.org/problems/find-the-closest-number5513/1
Question Name : find-the-closest-number
"""


from typing import List


class Solution:
    def findClosest(self, arr, k):
        # code here
        
        start = 0 
        end = len(arr) -1
        strtdiff = abs(k - arr[start])
        enddiff = abs(k - arr[end])
        moving = False
        if arr[start] == k or arr[end] == k :
                return k
        
        # mid = int (( start + end) / 2 )
        
        while start< end :
            if arr[start+1] == k or arr[end-1] == k :
                return k
            if  k > arr[start+1] and abs(k - arr[start+1]) <= strtdiff :
                strtdiff = abs(k - arr[start+1])
                start +=1
                moving = True
                
                
            if k < arr[end-1] and abs(arr[end-1]-k) <= enddiff :
                enddiff = abs(arr[end-1]-k)
                end -=1
                moving = True
            
            if moving== False : 
                break 
            
            moving = False
                
        # print(start)
        # print(end)
        
        if strtdiff == enddiff:
            return max(arr[start] , arr[end])
        elif strtdiff < enddiff:
            return arr[start]
        else:
            return arr[end]
            
        
                
        
        # return 0
        
