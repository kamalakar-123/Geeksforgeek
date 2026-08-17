class Solution:

	
	def removeDuplicates(self, s):
	    newstring=""
	    for ch in s:
	        if ch not in newstring:
	           newstring+=ch 
	    return newstring
	    