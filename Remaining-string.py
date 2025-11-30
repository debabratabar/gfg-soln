
"""
Question Link : https://www.geeksforgeeks.org/problems/remaining-string3515/1
Question Name : remaining-string
"""

class Solution:
	def printString(self, s, ch, count):
		# code here
		
		cnt = 0
		idx = -1
		for i in range(len(s)):
		    if cnt <count:
		        if s[i] == ch :
		            cnt+=1
					idx = i
		            
		            
		if idx < len(s) and cnt == count:
		     return s[idx+1:]
		     
		return ''
		            
		 