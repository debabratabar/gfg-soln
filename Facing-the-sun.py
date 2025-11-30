
"""
Question Link : https://www.geeksforgeeks.org/problems/facing-the-sun2126/1
Question Name : facing-the-sun
"""

#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        
        maxx = float('-inf')
        ans = 0
        
        for i in range(0 , len(height)):
            if i !=0 :
                if height[i] > height[i-1]  and height[i] > maxx:
                    ans+=1
                    maxx = height[i]
                
            else :
                ans=1
                maxx = height[i]
                
        
        # print(ans)
        
        return ans