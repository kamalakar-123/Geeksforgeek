class Solution:
    def minValueToBalance(self, arr: list[int]) -> int:
        # code here
        left=[]
        right=[]

        size=len(arr)
        left=arr[:size//2]
        right=arr[size//2:]

        leftsum=sum(left)
        rightsum=sum(right)

        return abs(leftsum-rightsum)