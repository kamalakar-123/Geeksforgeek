from math import factorial
class Solution:
    def nPr(self, n: int, r: int) -> int:
        # code here
        return factorial(n)//factorial(n - r)