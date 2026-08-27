class Solution:
    def checkElements(self, start, end, arr):
        # code here
        arr1=set(arr)
        for i in range(start,end+1):
            if i not in arr1:
                return False
        return True