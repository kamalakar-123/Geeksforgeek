class Solution:
    def findMedian(self, arr):
        arr.sort()
        length = len(arr)
        mid =  length // 2
        if length == 0:
            return None
        else:
            if length % 2 != 0:
                return arr[mid]
            else:
                return (arr[mid] + arr[mid - 1])/2