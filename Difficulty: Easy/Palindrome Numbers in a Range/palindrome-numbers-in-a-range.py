class Solution:
    def printPalindromes(self, m, n):
        # code here
        ans=[]
        for i in range(m,n+1):
            if i==int(str(i)[::-1]):
                ans.append(i)
                
                
        return ans