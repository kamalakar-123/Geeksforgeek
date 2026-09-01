class Solution:
    def xorArray(self, arr):
        # code here
        newarr=[]
        for i in range(len(arr)-1):
            newarr.append(arr[i]^arr[i+1])
        newarr.append(arr[-1])
            
        return newarr