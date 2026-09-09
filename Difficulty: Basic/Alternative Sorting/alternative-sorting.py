class Solution:
    def alternateSort(self, arr):
        # code here
        arr.sort()
        i=0
        j=len(arr)-1
        newarr=[]
        while i<j:
            newarr.append(arr[j])
            newarr.append(arr[i])
            i+=1
            j-=1
        if i==j:
            newarr.append(arr[i])
        return newarr