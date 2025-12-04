"""
Question Link : https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1
Question Name : String Rotated by 2 Places

"""

class Solution:
    def isRotated(self,s1,s2):
        #code here
        if len(s1) != len(s2):
            return False
            
        if len(s1)<3 and s1==s2 :
            return True
        if len(s1)<3 and s1!=s2 :
            return False
            
        rotate1 = s1[2:] + s[0]+s[1]
        rotate2 =  s1[len(s1)-2] +s1[len(s1)-1] + s1[0:len(s1)-2] 
        
        # print(rotate1)
        # print(rotate2)
        
        if rotate1 == s2 or rotate2== s2:
            return True
            
        return False