class Solution:
    def findElements(self,arr):
        # code here
        arr.sort()
        n=len(arr)
        return arr[0:n-2]
