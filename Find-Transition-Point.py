"""
Question Link : https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1


"""

class Solution:
    def transitionPoint(self, arr): 
        # Code here
        
        start = 0 
        end = len(arr) -1 
        hasOne=False
        
        mid = int((start+end) / 2 )
        
        
        while start <= end:
            if arr[mid] ==1:
                end = mid -1
                hasOne = True
                
            else:
                start = mid+1
            
            mid = int((start+end)/2)
            
        if hasOne :
            return start 
            
        return -1