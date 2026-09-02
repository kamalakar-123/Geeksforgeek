class Solution:
    def sumOfMatrix(self, mat: list[list[int]]) -> int:
        # code here
        total=0
        for i in mat:
            total=total+sum(i)
        return total