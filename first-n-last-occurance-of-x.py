
"""
Question Link : https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x2041/1
Question Name : first-n-last-occurance-of-x
"""


# User function Template for python3
class Solution: 
    
    
    def firstOcc(self , v, n ,  x):
        start = 0 
        end = n-1
        mid = int( (start+end)/2 )
        idx = -1
        
        while start <= end:
            if  x == v[mid]:
                idx = mid 
                end = mid -1
                
            elif x > v[mid] :
                start = mid+1
                
                
            else:
                end = mid - 1
                
                
        
            mid = int( (start+end)/2 )
        
        
        return idx; 
        
        
    def lastOcc( self ,v, n ,  x):
        start = 0 
        end = n-1
        mid = int( (start+end)/2 )
        idx = -1
        
        # print(v)
        
        while start <= end:
            if x == v[mid]:
                idx = mid 
                start = mid +1
                
            elif  x > v [mid] :
                start = mid+1
                
                
            else:
                end = mid - 1
                
                
        
            mid = int( (start+end)/2 )
        
        
        return idx; 
    
    def firstAndLast(self, x, arr): 
        # Code here
        
        n = len(arr) 
        
        first = self.firstOcc( arr , n ,  x)
        last = self.lastOcc( arr , n ,  x)
        
        # print(n)
        # print(first)
        # print(last)
        
        if first == -1 and last == -1:
            return [-1]
        
        
        return [first , last ]
        
        
        