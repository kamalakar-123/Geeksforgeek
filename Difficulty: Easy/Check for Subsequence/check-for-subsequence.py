class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        i=0
        for ch in s2:
            if i<len(s1) and s1[i]==ch:
                i+=1
        return i==len(s1)