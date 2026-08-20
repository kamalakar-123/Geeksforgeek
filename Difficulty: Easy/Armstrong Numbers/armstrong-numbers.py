class Solution:
    def armstrongNumber(self, n: int) -> bool:
        m = n
        result = 0
        while m > 0:
            last = m % 10
            result += last**3
            m //= 10
    
        return result == n