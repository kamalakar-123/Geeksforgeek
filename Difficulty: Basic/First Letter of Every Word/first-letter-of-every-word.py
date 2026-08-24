class Solution:
	def firstAlphabet(self, s):
		# code here
		newstr=s.split()
		news=""
		for i in newstr:
		    x=i[0]
		    news=news+x
		return news