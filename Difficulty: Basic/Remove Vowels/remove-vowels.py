class Solution:
	def removeVowels(self, s):
		# code here
		news=""
		for ch in s:
		    if ch in "aeiou":
		        continue
		    news=news+ch
		return news