class Solution:
    def longest(self, arr):
        # code here
        longest = arr[0]

        if len(arr)>0:

            for i in arr:
                if len(i) > len(longest):
                    longest = i

            return longest