class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        res=0
        for i in str(n):
            res=res+int(i)
        z=str(res)
        l=z[::-1]
        if res==int(l):
            return True
        else:
            return False