
"""
Question Link : https://www.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1
Question Name : sum-of-numbers-in-string
"""

class Solution:
    def findSum(self, s):
        #code here
        #code here
        num = ''
        # digit = 0
        sum=0
        
        for i in s:
            if i.isdigit():
                num +=i
            else:
                if num !='':
                    sum+=int(num)
                    num=''
    
    
        if num !='':
            sum+=int(num)
    
        # print(int(num))
        # print(sum)
        
        return sum  
                    