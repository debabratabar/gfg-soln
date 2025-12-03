"""
Question Link : https://www.geeksforgeeks.org/problems/k-largest-elements4206/1
Question Name : k largest elements

"""

class Solution:
	def kLargest(self, arr, k):
		# Your code here
		
		arr.sort()
		
		res = []
		
		for i in range( -1 , -1-k,-1):
		    res.append(arr[i])
		    
	    return res